# Sachiko-chan
Một con Bot Discord, ẩn dưới dạng một cô gái Anime với "[kiểu nói chuyện cuties UwU](https://www.urbandictionary.com/define.php?term=UwU%20Speech)" và cô ấy rất hay sử dụng [emoji](https://vi.wikipedia.org/wiki/Emoticon#Japanese_(kaomoji)) khi nhắn tin.

Sachiko-chan sử dụng [API của OpenAI](https://platform.openai.com/docs/api-reference/chat) và [Pycord](https://pycord.dev) để vận hành, và được làm hoàn toàn từ ~~trái tim của 1 thằng wibu ráck đéo có gái như tôi~~ sự thấu hiểu tâm tư của mấy khứa SIMP từ 1 người đã chạm cỏ lâu năm như tôi...

## How to chạy Bot
Để chạy Sachiko-chan cho riêng mình, hãy đảm bảo rằng bạn đã cài Python 3.8 hoặc phiên bản cao hơn cùng với pip về máy tính của bạn. Bạn có thể tải Python [tại đây](https://www.python.org/downloads/).
Nếu sử dụng điện thoại Android, hãy thử [UserLAnd](https://userland.tech/) hoặc [Termux](https://termux.dev/), 2 ứng dụng này sẽ giúp bạn giả lập các chuỗi hệ điều hành Unix mà không cần Root máy.
Nếu bạn sử dụng điện thoại iOS, hãy thử sử dụng [iSH Shell](https://apps.apple.com/us/app/ish-shell/id1436902243), ứng dụng này sẽ giúp bạn giả lập hệ điều hành Alpine Linux mà không cần Jailbreaks.

Bạn sẽ phải khởi tạo 1 ứng dụng tại trang Web dành cho Developer của Discord: [Discord Developer Portal](https://discord.com/developers/applications), và tạo 1 con Bot trong ứng dụng của bạn. Và [đây](https://discordpy.readthedocs.io/en/stable/discord.html) là hướng dẫn để làm việc đó.

Bạn cũng cần phải có mã key OpenAI API để Bot có thể hoạt động, bạn có thể lấy mã đó bằng cách tạo tài khoản OpenAI - ChatGPT [tại đây](https://beta.openai.com/).

1. Dùng [git](https://git-scm.com/) để clone dự án này về máy bằng lệnh `git clone https://github.com/dragonx943/sachiko-chan`, hoặc ấn chọn Code -> Download ZIP từ trang GitHub (cần phải giải nén).
2. Mở thư mục sachiko-chan (Linux thì dùng lệnh `cd sachiko-chan` để điều hướng về thư mục của Bot)
3. Cài đặt những thư viện cần thiết cho python bằng lệnh:

    ```sh
    pip install -r requirements.txt
    ```

4. Tạo 1 tệp `.env` tại thư mục của Bot hoặc đổi tên file `.env.example` thành `.env`, và thêm những dòng sau vào tệp đó (sử dụng các trình soạn file như Notepad++,...):

    ```
    DISCORD_TOKEN=<Nhập mã Discord Token bạn lấy ở trang Discord Developer Portal vào đây>
    OPENAI_API_KEY=<Nhập mã key OPENAI API bạn lấy ở trang OPENAI vào đây>
    ```

5. Chạy Bot bằng lệnh:

    ```sh
    python main.py
    ```

==> Bạn có thể chỉnh lại mẫu prompt nhân vật (cách phản hồi của ChatGPT) tại file **prompt.txt** để sửa đổi cách nói chuyện, tính cách, hình mẫu,...của ChatGPT, từ đó tự tạo ra nhân vật Anime của chính mình muốn!

==> Bạn cũng có thể dùng Bot tôi đã tạo sẵn ở đây, Bot sẽ được Host và vá lỗi liên tục: https://top.gg/bot/1203719197088292884 và https://top.gg/bot/1256459064179691641

## Đóng góp
Vui lòng đóng góp tại trang Github dự án gốc của bemxio về Sachiko-chan: [bemxio/sachiko-chan](https://github.com/bemxio/sachiko-chan)
