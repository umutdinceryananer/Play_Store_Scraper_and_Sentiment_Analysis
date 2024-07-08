import subprocess

# scraper.py dosyasını çalıştır
print("Veri çekiliyor ve sentiment analizi yapılıyor...")
subprocess.run(["python", "scraper.py"])

# sentiment_analysis.py dosyasını çalıştır
print("Grafik oluşturuluyor...")
subprocess.run(["python", "sentiment_analysis.py"])

print("Tüm işlemler tamamlandı.")
