# Google Play Store Uygulama Yorumları için Duygusallık Analizi

Bu proje, Google Play Store'da yer alan uygulamalar için yapılan son 1000 İngilizce yorumu çekip, bu yorumları sentiment analizinden geçirerek bir histogram grafiği oluşturur.
> Yapılan yorum sayısı programda 1000 olarak kabul edilmiştir ama modelin sonuç süresi göz önüne alınarak sayı arttırılabilir.

Sentiment Analysis için Kullanılan Model: [SiEBERT - English-Language Sentiment Classification](https://huggingface.co/siebert/sentiment-roberta-large-english)

Sentiment Analiz modeli için SiEBERT seçilmiş olmasının sebebi İngilizce metin değerlendirmelerinde en tutarlı model olması ve Türkçe Sentiment Analizi 
için geliştirilen modellerin henüz yeterince tutarlı sonuçlar verememesidir.

## Gereksinimler:
* Python 3.x
  - Gerekli Python kütüphaneleri:
    - google-play-scraper
    - transformers
    - pandas
    - emoji
    - re
    - plotly

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
```
pip install -r requirements.txt
```

### Dosya Açıklamaları:
** scraper.py **
Bu dosya, Google Play Store'dan yorumları toplar ve sentiment analizini yapar. Çıktı olarak wonder_reviews_raw.json dosyasını oluşturur.

** sentiment_analysis.py **
Bu dosya, scraper.py tarafından oluşturulan JSON dosyasını kullanarak veriyi işler ve grafik oluşturur. Çıktı olarak sentiment_histogram.html dosyasını oluşturur.

### Kullanım:
Tüm işlemleri tek bir komutla çalıştırmak için aşağıdaki komutu kullanın:
```
!python run_all.py
```
Bu komut sonrası 1000 yorum için ortalama olarak **7 dakikalık bir bekleme süresi** sonucu çıktılara ulaşılabiliyor.

Program örnek olarak Codeway tarafından geliştirilen Wonder AI uygulamasını kullanıyor. 
Başka uygulamalar için scraper.py dosyası içinde 9. satırda yer alan Product ID değiştirilebilir. -> 'com.codeway.wonder'
Örnek olarak; Ask AI - Chat with AI Chatbot uygulaması için Play Store URL'sinden "com.codeway.chatapp" kısmı scraper.py içinde değiştirilebilir.

Bu komut, önce scraper.py dosyasını çalıştırarak yorumları çeker ve sentiment analizini yapar, ardından sentiment_analysis.py dosyasını çalıştırarak yorumlardan elde edilen verilerle bir histogram grafiği oluşturur.

>[!NOTE]
>Grafik, sentiment_histogram.html dosyası olarak kaydedilecektir.

### Çıktılar:
wonder_reviews_raw.json: Çekilen ve sentiment analizi yapılan ham yorumlar.
wonder_reviews_processed.json: İşlenmiş ve sentiment analiz sonuçları ayrıştırılmış yorumlar.
sentiment_histogram.html: Yorumlardan elde edilen verilerle oluşturulan histogram grafiği.

### İletişim:
Eğer bir sorunuz veya geri bildiriminiz varsa, bana ulaşmayı tercih etmeniz beni çok mutlu eder.

E-posta: umutdncr@gmail.com
LinkedIn: https://www.linkedin.com/in/umut-yananer/

---

# Sentiment Analysis for Google Play Store App Reviews

This project creates a histogram chart by pulling the last 1000 English comments for applications on the Google Play Store and passing these comments through sentiment analysis.
> The number of comments made is accepted as 1000 in the program, but the number can be increased considering the result time of the model.

Model Used for Sentiment Analysis: [SiEBERT - English-Language Sentiment Classification](https://huggingface.co/siebert/sentiment-roberta-large-english)

SiEBERT was chosen for the Sentiment Analysis model because it is the most consistent model in English text evaluations and Turkish Sentiment Analysis
The reason is that the models developed for this are not yet able to provide sufficiently consistent results.

## Requirements:
* Python 3.x
 - Required Python libraries:
 - google-play-scraper
 -transformers
 -pandas
 - emoji
 -re
 - plotly

Run the following command to install the required libraries:
```
pip install -r requirements.txt
```

### File Descriptions:
** scraper.py **
This file collects comments from Google Play Store and performs sentiment analysis. It produces wonder_reviews_raw.json as output.

** sentiment_analysis.py **
This file processes the data and creates graphs using the JSON file created by scraper.py. It creates the sentiment_histogram.html file as output.

### Use:
To run all processes with a single command, use the following command:
```
!python run_all.py
```
After this command, the output can be obtained as a result of an average of **7 minutes waiting time** for 1000 comments.

The program uses the Wonder AI application developed by Codeway as an example.
For other applications, the Product ID on line 9 in the scraper.py file can be changed. -> 'com.codeway.wonder'
For example; For the Ask AI - Chat with AI Chatbot application, the "com.codeway.chatapp" part of the Play Store URL can be changed in scraper.py.

This command first runs the scraper.py file to extract comments and analyze sentiment, and then runs the sentiment_analysis.py file to create a histogram chart with the data obtained from the comments.

>[!NOTE]
>The chart will be saved as sentiment_histogram.html file.

### Outputs:
wonder_reviews_raw.json: Raw reviews captured and sentiment analyzed.
wonder_reviews_processed.json: Processed reviews and parsed sentiment analysis results.
sentiment_histogram.html: Histogram chart created with data obtained from comments.

### Communication:
If you have any questions or feedback, I would be very happy if you choose to reach out to me.

Email: Umutdncr@gmail.com
LinkedIn: https://www.linkedin.com/in/umut-yananer/
