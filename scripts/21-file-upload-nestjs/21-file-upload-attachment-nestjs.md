# NestJS #21 — File Upload: đừng tin chiếc đuôi `.jpg`

- **Series:** Học NestJS bằng AI — tập 21/45
- **Target runtime:** khoảng 6 phút (573 từ thoại)
- **Outcome:** Upload attachment có auth, giới hạn dung lượng, kiểm tra magic bytes và lưu object storage an toàn.
- **Pain tập kế:** File và dữ liệu tăng khiến GET `/tasks` trả quá nhiều bản ghi.

---

## PART 1 — SCRIPT

User báo lỗi task, nhưng TaskFlow không cho họ đính kèm ảnh.

Mình thêm upload. Năm phút sau, một file tên `error.jpg` đi thẳng vào storage.

Bên trong nó không phải ảnh.

Mình từng kiểm tra extension và MIME type do trình duyệt gửi lên.

Cả hai đều là lời khai của client. Client thì có thể nói dối rất tự tin.

Đổi tên một file lạ thành `.jpg` không biến nó thành ảnh.

Bước ngoặt là coi file upload như dữ liệu không tin cậy, giống request body.

Magic bytes là vài byte đầu nhận diện định dạng thật của file.

Nó giống kiểm tra hàng bên trong, thay vì tin nhãn dán ngoài thùng.

Mình đưa AI requirement: attachment cho task, tối đa năm megabyte, chỉ JPEG và PNG.

AI lập plan dùng Multer và lưu file vào thư mục `uploads` của server.

Mình dừng ở bước review.

Local disk chạy tốt trên laptop, nhưng có thể biến mất khi container được thay mới.

Nhiều instance cũng không nhìn thấy cùng một ổ đĩa.

Mình approve thiết kế dùng object storage tương thích S3 và database chỉ giữ metadata.

Controller dùng `FileInterceptor` để nhận multipart form-data.

`ParseFilePipe` chặn file thiếu và dung lượng vượt giới hạn sớm.

Nhưng `FileTypeValidator` mặc định vẫn dựa trên loại file Multer phát hiện.

Với boundary nhạy cảm, mình đọc buffer và kiểm tra magic bytes lần nữa.

Chỉ khi định dạng thật nằm trong allowlist, file mới được lưu.

Tên gốc chỉ dùng để hiển thị sau khi làm sạch.

Storage key do server tạo bằng UUID. Người dùng không được quyết định đường dẫn.

Nếu lấy nguyên `../../avatar.jpg`, chúng ta vừa mời path traversal vào nhà.

Attachment cũng thuộc về một task.

Permission `tasks.update` chưa đủ. Service phải kiểm tra ownership hoặc scope dự án.

Avatar dùng cùng storage adapter, nhưng có route và policy riêng.

Mình không tạo một endpoint “upload mọi thứ” cho tiện.

Mình đặt rule này trước thao tác upload để user lạ không đốt bandwidth storage.

Sau khi upload thành công, repository lưu object key, tên hiển thị, kích thước và content type thật.

Không lưu public URL cố định trong database.

Khi tải xuống, API kiểm tra quyền rồi mới tạo signed URL ngắn hạn.

Nếu database insert thất bại sau khi object đã lên, mình xóa object để tránh file mồ côi.

Đây chưa phải distributed transaction. Nó là cleanup có chủ đích và có log.

Mình chạy ba ca kiểm chứng.

Ảnh PNG thật được chấp nhận. File quá lớn trả bốn-một-ba.

File text đổi tên thành `.jpg` trả bốn-hai-hai.

Một user khác xin download attachment nhận bốn-không-ba.

Cuối cùng, mình mở object storage. Không có tên file do người dùng điều khiển.

Log có attachment ID, không có nội dung file hay signed URL đầy đủ.

Upload không chỉ là nhận một buffer. Nó là một chuỗi trust boundary.

Mỗi lần hệ thống nhận dữ liệu, mình phải quyết định phần nào đáng tin.

TaskFlow đã nhận được file. Bây giờ năm nghìn task lại kéo response xuống đáy.

Tập sau, mình sẽ phân trang bằng cursor ổn định, không chỉ cắt mảng cho đẹp.

Nếu bạn muốn xây những boundary production ít ai nhắc, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [TERM] | Upload `error.jpg`, dùng `file`/hex viewer cho thấy nội dung không phải ảnh | 25s |
| 2 | [DIAGRAM] | Nhãn file so với magic bytes bên trong | 25s |
| 3 | [BROWSER] | Review plan lưu `uploads/` local; highlight vấn đề container và multi-instance | 30s |
| 4 | [DIAGRAM] | Client → Controller → validation → object storage + metadata DB | 30s |
| 5 | [IDE] | `FileInterceptor`, `ParseFilePipe`, size limit và Swagger multipart | 40s |
| 6 | [IDE] | Hàm kiểm tra magic bytes và allowlist JPEG/PNG | 35s |
| 7 | [IDE] | UUID storage key, sanitize display name, ownership trước upload | 35s |
| 8 | [IDE] | Lưu metadata; cleanup object nếu insert DB fail | 30s |
| 9 | [DIAGRAM] | Download qua permission check và signed URL ngắn hạn | 30s |
| 10 | [TERM] | Test ảnh thật, file quá lớn, fake JPG và user sai quyền | 45s |
| 11 | [BROWSER] | Task detail hiển thị attachment hợp lệ; network không lộ storage credential | 20s |
| 12 | [B-ROLL] | Object key ngẫu nhiên, cut sang danh sách hàng nghìn task | 15s |

**Tổng mục tiêu: 6 phút.** One Dark Pro, font 18–20px. Chỉ dùng file test vô hại; che bucket, signed URL và credential.

### Code cốt lõi

```ts
@Post(':taskId/attachments')
@UseInterceptors(FileInterceptor('file', { limits: { fileSize: 5_000_000 } }))
@ApiConsumes('multipart/form-data')
upload(
  @Param('taskId') taskId: string,
  @UploadedFile(new ParseFilePipeBuilder().addMaxSizeValidator({
    maxSize: 5_000_000,
  }).build())
  file: Express.Multer.File,
  @CurrentUser() user: AuthUser,
) {
  return this.attachmentsService.upload({ taskId, user, file });
}
```

```ts
const detected = await fileTypeFromBuffer(file.buffer);
if (!detected || !['image/jpeg', 'image/png'].includes(detected.mime)) {
  throw new UnprocessableEntityException('Unsupported file content');
}
const objectKey = `tasks/${taskId}/${randomUUID()}.${detected.ext}`;
```

### Prompt cho AI

```text
Plan secure task attachments for the current NestJS API.
- Accept JPEG and PNG up to 5 MB through multipart/form-data.
- Enforce authentication, tasks.update permission and ownership before storage work.
- Reuse the storage adapter for avatars, but keep a separate route and validation policy.
- Treat extension and client MIME type as untrusted; verify magic bytes.
- Generate the storage key server-side and sanitize the display filename.
- Store objects in S3-compatible storage and only metadata in PostgreSQL.
- Authorize downloads before issuing a short-lived signed URL.
- Define cleanup when object upload succeeds but metadata persistence fails.
- Add tests for fake extensions, oversize files, unauthorized access and cleanup.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right holding an image file whose peeled-back label reveals suspicious binary content, dark monitor glow, deep black and navy background with NestJS red-pink #E0234E accents, empty left space for headline text, 16:9, photorealistic, no text.`
2. `A cinematic photograph of a dark upload pipeline scanning a glowing file at a security checkpoint before object storage, developer silhouette on the right, NestJS red-pink #E0234E rim light, empty dark left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer watching a fake JPG file get rejected by a red security gate on a dark code monitor, subject on the right, black and dark navy scene, NestJS red-pink #E0234E highlights, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. File Upload NestJS: Đừng tin đuôi .JPG — EP21 | Lập trình là cuộc sống
2. Một file giả danh ảnh đi vào production — EP21 | Lập trình là cuộc sống
3. Upload ảnh an toàn với Magic Bytes — EP21 | Lập trình là cuộc sống
4. Vì sao không nên lưu Upload trong Container? — EP21 | Lập trình là cuộc sống
5. Attachment, Object Storage và Signed URL — EP21 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1. A/B test Title 2 cho curiosity.

### 4b. SEO Description

```text
Extension và MIME type đều là lời khai của client. Tập 21 xây attachment cho TaskFlow mà không tin chiếc đuôi .jpg.

✅ Nhận multipart bằng FileInterceptor
✅ Chặn file quá dung lượng
✅ Kiểm tra magic bytes thay vì tin extension
✅ Tạo object key phía server
✅ Tách object storage và metadata database
✅ Bảo vệ upload/download bằng permission và ownership
✅ Cleanup file mồ côi khi lưu metadata lỗi

🔗 NestJS File Upload: https://docs.nestjs.com/techniques/file-upload
🔗 OWASP File Upload Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

⏱ 0:00 File JPG không phải ảnh
⏱ 0:35 Magic bytes
⏱ 1:10 Vì sao local disk không đủ
⏱ 1:55 FileInterceptor và size limit
⏱ 2:45 Kiểm tra nội dung thật
⏱ 3:35 Ownership và storage key
⏱ 4:20 Metadata, cleanup và signed URL
⏱ 5:10 Bốn ca kiểm chứng

#NestJS #FileUpload #ObjectStorage #MagicBytes #APISecurity #TypeScript #Backend #Production #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs file upload, multer nestjs, secure file upload nodejs, magic bytes file validation, fake jpg upload, nestjs object storage, s3 signed url nestjs, attachment api nestjs, parse file pipe nestjs, file size validator nestjs, path traversal upload, upload ownership authorization, taskflow nestjs, học nestjs bằng ai, nestjs tập 21, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `ĐỪNG TIN` — WHITE `#FFFFFF`
- `.JPG` — NEST RED `#E0234E`
- Badge nhỏ: `EP 21`

### Option 2
- `FILE NÀY` — WHITE `#FFFFFF`
- `ĐANG NÓI DỐI` — NEST RED `#E0234E`
- Badge nhỏ: `UPLOAD`

### Option 3
- `CHECK RUỘT` — WHITE `#FFFFFF`
- `ĐỪNG CHECK TÊN` — NEST RED `#E0234E`
- Badge nhỏ: `MAGIC BYTES`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
