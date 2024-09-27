from datetime import datetime

def get_zodiac_sign(day, month):
    zodiac_signs = [
        (120, "Capricorn"), (218, "Aquarius"), (320, "Pisces"), (420, "Aries"), (521, "Taurus"),
        (621, "Gemini"), (722, "Cancer"), (823, "Leo"), (923, "Virgo"), (1023, "Libra"),
        (1122, "Scorpio"), (1222, "Sagittarius"), (1231, "Capricorn")
    ]
    date_number = month * 100 + day
    for z_sign in zodiac_signs:
        if date_number <= z_sign[0]:
            return z_sign[1]

def calculate_age(birthdate):
    today = datetime.today()
    umur = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return umur

def get_zodiac_quote(zodiac_sign):
    try:
        # Nama file sesuai dengan zodiak, misalnya "Capricorn.txt"
        with open(f'qoute/{zodiac_sign}.txt', 'r') as file:
            quote = file.read().strip()  # Membaca seluruh isi file dan menghilangkan spasi di awal/akhir
        return quote
    except FileNotFoundError:
        return f"Tidak ada kata-kata mutiara untuk zodiak {zodiac_sign}."

def main():
    # Validasi Input nama
    name_str= ""
    while not name_str:
        name_str = input("Masukan Nama Anda")
        
        if not name_str:
            print("Nama Anda tidak boleh kosong. silahkan coba lagi.")


    # Validasi input tanggal lahir
    birthdate_str = ""
    while not birthdate_str:
        birthdate_str = input("Masukkan tanggal lahir (DD-MM-YYYY): ").strip()
        if not birthdate_str:
            print("Tanggal lahir tidak boleh kosong. Silakan coba lagi.")
            continue
        # Cek apakah format tanggal benar
        try:
            birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
        except ValueError:
            print("Format tanggal salah. Gunakan format DD-MM-YYYY.")
            birthdate_str = ""  # Reset input jika format salah

    day = birthdate.day
    month = birthdate.month

    zodiac = get_zodiac_sign(day, month)
    umur = calculate_age(birthdate)
    quote = get_zodiac_quote(zodiac)

    # Output dengan nama, zodiak, umur, tanggal lahir, dan kata-kata mutiara
    print(f"\nHalo, {name_str}!")
    print(f"Tanggal lahir Anda: {birthdate.strftime('%d-%m-%Y')}")
    print(f"Zodiak Anda: {zodiac}")
    print(f"Umur Anda: {umur} tahun")
    print(f"Kata-kata mutiara untuk {zodiac}: {quote}")

if __name__ == "__main__":
    main()
