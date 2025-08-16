````markdown

## Kurulum

Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
````

## Uygulamayı Çalıştırma

### Seçenek 1: GitHub API ile (Varsayılan)

Bu varsayılan ayardır ve GitHub API ile çalışır. Uygulamayı şu şekilde başlatabilirsiniz:

```bash
python start_servers.py
```

Sonra başka bir terminalde:

```bash
streamlit run app.py
```

### Seçenek 2: OpenAI API ile

Uygulamayı OpenAI API ile çalıştırmak isterseniz, aşağıdaki değişiklikleri yapın:

`app.py` içinde şunu:

```python
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com"
)
```

şununla değiştirin:

```python
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)
```

`translation_server.py` içinde şunu:

```python
client = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com"
)

def gpt_call(messages, model="gpt-4o-mini", temperature=None):
    response = client.invoke(messages, model=model, temperature=temperature)
    return response.content.strip()
```

şununla değiştirin:

```python
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def gpt_call(messages, model="gpt-4o", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()
```

### Seçenek 3: Terminal sürümü

Uygulamayı terminal üzerinden çalıştırmak isterseniz:

```bash
python terminal_github.py
```
