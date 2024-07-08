from google_play_scraper import Sort, reviews
from transformers import pipeline
import pandas as pd
import emoji
import re

# İlk 1000 yorumu çekme
result, continuation_token = reviews(
    'com.codeway.wonder',
    lang='en', 
    country='us', 
    sort=Sort.NEWEST, 
    count=1000,
)

num_reviews = len(result)
#print(f'Total reviews scraped: {num_reviews}')

def replace_emoji_with_text(text):
    return emoji.demojize(text)

def contains_text(text):
    return bool(re.search(r'\w', text))

# Emojili yorumları saymak için variable listesi
emoji_count = 0
text_and_emoji_count = 0
emoji_only_count = 0

for review in result:
    original_content = review['content']
    new_content = replace_emoji_with_text(original_content)
    if original_content != new_content:
        emoji_count += 1
        if contains_text(original_content):
            text_and_emoji_count += 1
        else:
            emoji_only_count += 1
    review['content'] = new_content

df = pd.DataFrame(result)

# Veri tiplerini check etme
#print(df.dtypes)

# Veri tiplerini stringe çevirme
df['content'] = df['content'].fillna('NaN').astype(str)

# Veri tiplerini tekrar kontrol et (String dönüşümü başarılı mı diye kontrol)
#print(df.dtypes)

# İşleme sokulmayan sütunlar burada siliniyor.
df.drop(columns=['userImage', 'appVersion', 'thumbsUpCount', 'reviewId', 'at', 'replyContent', 'repliedAt', 'userName'], inplace=True)

sentiment_analysis = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

df['sentiment'] = df['content'].apply(lambda x: sentiment_analysis(x)[0])

df.to_json('wonder_reviews_raw.json', orient='records', lines=True, force_ascii=True)

#print(f'Total reviews with emojis: {emoji_count}')
#print(f'Total reviews with both text and emojis: {text_and_emoji_count}')
#print(f'Total reviews with only emojis: {emoji_only_count}')
#print('Reviews have been saved')

#print(df['reviewCreatedVersion'].value_counts().sort_index(ascending=False))  # Versiyonlara göre yapılan yorumların listesi
