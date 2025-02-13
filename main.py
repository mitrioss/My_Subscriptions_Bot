from decouple import config

TELEGRAM_BOT_KEY = config('TELEGRAM_BOT_KEY')

def main():
    print(f"Программа успешно запущена! {TELEGRAM_BOT_KEY}")

if __name__ == "__main__":
    main()