import pandas as pd
import plotly.express as px

# JSON dosyasını burada yüklüyoruz.
df = pd.read_json('wonder_reviews_raw.json', lines=True)

# Label ve score sütunlarını ayırma
df['sentiment_type'] = df['sentiment'].apply(lambda x: x['label'])
df['sentiment_score'] = df['sentiment'].apply(lambda x: x['score'])

# Artık gerek olmayan eski sentiment sütununu kaldırma
df.drop(columns=['sentiment'], inplace=True)

# Güncellenmiş veri çerçevesini kaydetme
df.to_json('wonder_reviews_processed.json', orient='records', lines=True)

#print(df['sentiment_type'].value_counts())

fig = px.histogram(df, x='sentiment_type', color='sentiment_type', text_auto=True)

def normalize_sentiment(row):
    if row['sentiment_type'] == 'POSITIVE':
        return row['sentiment_score'] * 5
    elif row['sentiment_type'] == 'NEGATIVE':
        return row['sentiment_score'] * 1  # NEGATIVE için 1 üzerinden normalleştirme
    else:
        return row['sentiment_score'] * 3  # NEUTRAL için ortalama 3

df['normalized_sentiment'] = df.apply(normalize_sentiment, axis=1)
average_normalized_sentiment = df['normalized_sentiment'].mean()
#print(f"Sentiment analiz sonuçları 5 üzerinden normalize edilmiş ortalama değer: {average_normalized_sentiment:.2f}")

average_score = df['score'].mean()
#print(f"Sentiment analizi uygulanmadan sadece Play Store değerlendirmelerinin ortalaması: {average_score:.2f}")

fig.update_layout(
    title=f'<b>Wonder AI Uygulaması için Play Store içinde yapılan son 1000 İngilizce Yorumun Duygusallık Analiz Sonucu</b><br>Google Play Store Son 1000 Yorum Ortalaması: {average_score:.2f}                  Sentiment Analiz Son 1000 Yorum Ortalaması: {average_normalized_sentiment:.2f}',
    xaxis_title='Duygusal Analiz Sonuç Tipi',
    yaxis_title='Yorum Miktar',
)

# Grafiği HTML dosyasına kaydetmek için kod
fig.write_html("sentiment_histogram.html")

# İşlem Tamamlandı Mesajı
print("Grafik 'sentiment_histogram.html' dosyasına kaydedildi. Tarayıcınızda açabilirsiniz.")
