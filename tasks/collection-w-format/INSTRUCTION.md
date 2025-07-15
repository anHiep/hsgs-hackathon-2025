# Hướng dẫn tổng hợp đề thi

## Mục tiêu  
Tổng hợp và chuẩn hóa đề thi từ các nguồn khác nhau để có thể đăng lên hệ thống Canvas.

## Nội dung thực hiện
Thoải mái tuỳ vào cách làm và công cụ mà bạn muốn dùng.

Các phần code có thể được thực hiện ngay tại folder ```collection-w-format```.

Các đề được tổng hợp và chuẩn hoá phải được lưu tại folder ```bank``` và subfolder ```math, listening, reading``` tương ứng, mỗi đề trong một file txt riêng biệt, riêng các đề listening thì phải lưu 2 file txt và mp3 có tên giống nhau (ví dụ: task1.txt ~ task1.mp3)

## Các bước thực hiện (gợi ý)

**Bước 1. Thu thập đề thi**  
Sử dụng công cụ tìm kiếm tự động hoặc thủ công để thu thập đề ở các định dạng như: ảnh, PDF, DOCX, v.v.

**Bước 2. Chuyển đổi định dạng**  
Chuyển các định dạng không phải văn bản sang văn bản thuần.  
Gợi ý công cụ: [`markitdown`](https://github.com/microsoft/markitdown)

**Bước 3. Chuẩn hóa văn bản**  
Chuyển các câu hỏi thu thập được về đúng định dạng chuẩn để đăng lên Canvas.  
Định dạng được mô tả tại: [`text2qti`](https://github.com/gpoore/text2qti)

## Ví dụ định dạng chuẩn sau Bước 3

```
Quiz title: {tên của đề, chuyển sang tiếng anh, không dùng dấu cách}
Quiz description: {khuyến khích nêu rõ nguồn gốc + tên ban đầu ở đây}

1.  {Nội dung câu hỏi thứ 1}
[ ] {Lựa chọn 1}
[ ] {Lựa chọn 2}
[*] {Lựa chọn 3, đúng}
[ ] {Lựa chọn 4}

1.  {Nội dung câu hỏi thứ 2, ví dụ là một câu trả lời ngắn}
*   {Một khả năng của đáp án}
*   {Một khả năng của đáp án}
*   {Một khả năng của đáp án}
*   {Một khả năng của đáp án}
*   {Một khả năng của đáp án}
```