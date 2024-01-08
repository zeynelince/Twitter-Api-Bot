import random
import time

def metin_botu():
    kelimeler = [",", ".", "!", "?", ";", "...", "(", ")", "[", "]", "{", "}", ":", "-", "'","a", "b", "c", "]", "{", "}", ":", "-", "sevgi"]

    while True:
        yeni_cümle = " ".join(random.sample(kelimeler, random.randint(1, min(len(kelimeler),10)))) + "."

        with open("metin_botu_output.txt", "w", encoding='utf-8') as dosya:
            dosya.write(yeni_cümle + "\n")

        time.sleep(42)  # 30 saniye bekleme süresi

if __name__ == "__main__":
    metin_botu()


#    kelimeler = ["insanca", "yaşamak", "için", "unutulmadık ", ]
#    kelimeler = [",", ".", "!", "?", ";", "...", "(", ")", "[", "]", "{", "}", ":", "-", "'"]