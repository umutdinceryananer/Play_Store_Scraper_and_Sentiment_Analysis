# Play Store Uygulamaları için Yorumlarda Sentiment Analiz Yazılımı

Bu proje, Google Play Store'da yer alan uygulamalar için yapılan son 1000 İngilizce yorumu çekip, bu yorumları sentiment analizinden geçirerek bir histogram grafiği oluşturur.

Sentiment Analysis için kullanılan model SiEBERT - English-Language Sentiment Classification, (https://huggingface.co/siebert/sentiment-roberta-large-english)

Sentiment Analiz modeli için SiEBERT seçilmiş olmasının sebebi İngilizce metin değerlendirmelerinde en tutarlı model olması ve Türkçe Sentiment Analizi 
için geliştirilen modellerin henüz yeterince tutarlı sonuçlar verememesidir.

Gereksinimler:
1. Python 3.x
2. Gerekli Python kütüphaneleri:
    2.1 google-play-scraper
    2.2 transformers
    2.3 pandas
    2.4 emoji
    2.5 re
    2.6 plotly

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
pip install -r requirements.txt

Kurulum:
!pip install -r requirements.txt

Dosya Açıklamaları:
*** scraper.py ***
Bu dosya, Google Play Store'dan yorumları toplar ve sentiment analizini yapar. Çıktı olarak wonder_reviews_raw.json dosyasını oluşturur.

*** sentiment_analysis.py ***
Bu dosya, scraper.py tarafından oluşturulan JSON dosyasını kullanarak veriyi işler ve grafik oluşturur. Çıktı olarak sentiment_histogram.html dosyasını oluşturur.

Kullanım:
Tüm işlemleri tek bir komutla çalıştırmak için aşağıdaki komutu kullanın:
!python run_all.py
Bu komut sonrası ortalama olarak 7 dakikalık bir run süresi sonucu çıktıya ulaşılabiliyor.

Program örnek olarak Codeway tarafından geliştirilen Wonder AI uygulamasını kullanıyor. 
Başka uygulamalar için scraper.py dosyası içinde 9. satırda yer alan Product ID değiştirilebilir. -> 'com.codeway.wonder'
Örnek olarak; Ask AI - Chat with AI Chatbot uygulaması için Play Store URL'sinden "com.codeway.chatapp" kısmı scraper.py içinde değiştirilebilir.

Bu komut, önce scraper.py dosyasını çalıştırarak yorumları çeker ve sentiment analizini yapar, ardından sentiment_analysis.py dosyasını çalıştırarak yorumlardan elde edilen verilerle bir histogram grafiği oluşturur.

Grafik, sentiment_histogram.html dosyasına kaydedilecektir.

Çıktılar:
wonder_reviews_raw.json: Çekilen ve sentiment analizi yapılan ham yorumlar.
wonder_reviews_processed.json: İşlenmiş ve sentiment analiz sonuçları ayrıştırılmış yorumlar.
sentiment_histogram.html: Yorumlardan elde edilen verilerle oluşturulan histogram grafiği.

İletişim:
Eğer bir sorunuz veya geri bildiriminiz varsa, lütfen bana ulaşın:

E-posta: umutdncr@gmail.com
LinkedIn: https://www.linkedin.com/in/umut-yananer/
