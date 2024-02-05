# Sachiko-chan
Một con Bot Discord, ẩn dưới dạng một cô gái Anime với "[kiểu nói chuyện cuties UwU](https://www.urbandictionary.com/define.php?term=UwU%20Speech)" và cô ấy rất hay sử dụng [emoji](https://vi.wikipedia.org/wiki/Emoticon#Japanese_(kaomoji)) khi nhắn tin.

Được làm từ [OpenAI's API](https://platform.openai.com/docs/api-reference/chat) và [Pycord](https://pycord.dev), được làm hoàn toàn bằng ~~trái tim của 1 thằng wibu ráck đéo có gái như tôi~~ sự tò mò code và sự đần độn của tôi...

## How to chạy Bot
Để chạy Sachiko-chan cho riêng mình, hãy đảm bảo rằng bạn đã cài Python 3.8 hoặc phiên bản cao hơn về máy tính hoặc điện thoại của bạn. Bạn có thể tải Python [tại đây](https://www.python.org/downloads/).

Bạn sẽ phải khởi tạo 1 ứng dụng tại trang Web dành cho Developer của Discord: [Discord Developer Portal](https://discord.com/developers/applications), và tạo 1 con Bot trong ứng dụng của bạn. Và [đây](https://discordpy.readthedocs.io/en/stable/discord.html) là hướng dẫn để làm việc đó.

Bạn cũng cần phải có mã key OpenAI API để Bot có thể hoạt động, bạn có thể lấy mã đó bằng cách tạo tài khoản OpenAI - ChatGPT [tại đây](https://beta.openai.com/).

1. Dùng [git](https://git-scm.com/) để clone dự án này về máy bằng lệnh `git clone`, hoặc ấn chọn Code -> Download ZIP từ trang GitHub.
2. Mở thư mục sachiko-chan (Linux thì dùng lệnh `cd sachiko-chan` để điều hướng về thư mục của Bot)
3. Cài đặt những thư viện cần thiết cho python bằng lệnh `pip install -r requirements.txt`.
4. Tạo 1 tệp `.env` tại thư mục của Bot, và thêm những dòng sau vào tệp đó (sử dụng các trình soạn file như Notepad++,...):

    ```
    DISCORD_TOKEN=<Nhập mã Discord Token bạn lấy ở trang Discord Developer Portal vào đây>
    OPENAI_API_KEY=<Nhập mã key OPENAI API bạn lấy ở trang OPENAI vào đây>
    ```

5. Chạy Bot bằng lệnh `python .\src\main.py` (Linux thì đổi \ thành / là oki).

## Đóng góp
Nếu có đóng góp hay có vấn đề, hãy di chuyển sang trang Repo chứa dự án gốc của bemxio để đóng góp, đừng đóng góp tại trang Repo này của tôi=)
Trang Repo / Dự án gốc của bemxio về Sachiko-chan: [bemxio/sachiko-chan](https://github.com/bemxio/sachiko-chan)