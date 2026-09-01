# 🤖 Monkeytype Typing Bot

Um experimento de automação desenvolvido em Python com Selenium para
coletar palavras do Monkeytype e reproduzir a digitação em um
laboratório local.

O projeto foi criado principalmente para estudar automação de
navegadores, manipulação de páginas web, Selenium e medição de
velocidade de digitação.

> ⚠️ o projeto é **EXPERIMENTAL**
**O monkeytype foi utilizado apenas para extrair as palavras que aparecem no jogo - Facilitando a alimentação de palavras para o bot**

### Código de extração de palavras
```
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "words"))
)

print("Área das palavras encontrada!")


elementos = driver.find_elements(
    By.CSS_SELECTOR,
    "#words .word"
)

palavras = []

for elemento in elementos:
    texto = elemento.text.strip()

    if texto:
        palavras.append(texto)


print(f"Encontrei {len(palavras)} palavras!")
```


---

## 🎯 Objetivo

A ideia inicial era descobrir se seria possível criar um programa capaz
de:

1. Abrir o Monkeytype automaticamente;
2. Encontrar as palavras exibidas na página;
3. Extrair essas palavras;
4. Reproduzir a frase em outro ambiente;
5. Digitar caractere por caractere;
6. Medir o desempenho da digitação.

O resultado foi dividido em duas partes:

- `bot.py` → controla o navegador e executa a automação;
- `teste.html` → funciona como um laboratório local para testar a
  digitação.

---

## 🧠 Como funciona

O fluxo atual é:

```text
Monkeytype
    │
    ▼
Selenium abre o navegador
    │
    ▼
Localiza #words
    │
    ▼
Extrai as palavras
    │
    ▼
Monta uma frase
    │
    ▼
Abre teste.html
    │
    ▼
Coloca a frase no laboratório
    │
    ▼
Selenium digita caractere por caractere
    │
    ▼
Calcula desempenho
    │
    ├── WPM
    ├── Precisão
    ├── Erros
    └── Tempo
```


## 📂 Arquivos

### bot.py
É o programa principal.

Ele é responsável por:
 - iniciar o Chrome;
 - abrir o Monkeytype;
 - aceitar os cookies quando necessário;
 - localizar a área de palavras;
 - coletar as palavras;
 - montar a frase;
 - abrir o laboratório local;
 - inserir a frase;
 - controlar a digitação;
 - calcular os resultados;
 - mostrar os resultados no terminal e na página.

### teste.html
É o laboratório local do projeto.

Ele possui:
 - área para mostrar a frase;
 - campo de entrada;
 - área para mostrar os resultados.
 - A página existe para que o motor possa ser testado em um ambiente
controlado.

### ⚙️ Tecnologias
Python
Selenium
HTML
CSS
Google Chrome


## 🚀 Como executar
1. Instale o Python
Verifique pelo terminal:
python --version

2. Instale o Selenium
No PowerShell:
pip install selenium

3. Baixe o projeto
Clone o repositório:
git clone URL_DO_REPOSITORIO

Entre na pasta:
cd monkeytype.script

4. Execute
python bot.py
O Chrome será aberto automaticamente.

O programa irá dizer por padrão
Iniciando bot...
Monkeytype carregado!
Cookies aceitos!
Área das palavras encontrada!

Depois ele coleta as palavras e mostra a frase encontrada.

## 📊 Resultados

Depois da execução, o programa calcula:
WPM
Words Per Minute/palavras por minuto
O cálculo utiliza a convenção de:
5 caracteres = 1 palavra
A fórmula utilizada é:
WPM = (caracteres / 5) / minutos

Precisão
Calculada a partir da quantidade de caracteres corretos e erros.
Precisão = acertos / (acertos + erros) × 100

Tempo
O tempo é medido utilizando:
time.perf_counter()
Isso permite medir o intervalo da execução com alta precisão.

Erros
O projeto possui a estrutura para contabilizar erros durante a
digitação.

## ⌨️ Motor de digitação
A digitação não é enviada como uma frase inteira.
O programa percorre cada palavra e depois cada caractere:

for palavra in palavras:
    for caractere in palavra:
        campo.send_keys(caractere)

Entre os caracteres existe um pequeno intervalo configurável:

INTERVALO = 0.01
Isso permite experimentar diferentes velocidades de digitação.

## 🔎 Coleta das palavras

As palavras são encontradas utilizando o seletor:
#words .word

Depois o texto de cada elemento é extraído e armazenado em uma lista.

No final:
frase = " ".join(palavras)
transforma as palavras em uma única frase.

## 🧪 Por que existe um laboratório local?
Durante o desenvolvimento, testar diretamente em uma aplicação externa
tornou o processo mais complicado.

Por isso foi criado o teste.html.
Ele permite controlar completamente o ambiente de teste e facilita
a investigação de:

entrada de teclado;
velocidade;
cálculo de WPM;
precisão;
erros;
comunicação entre Selenium e JavaScript/HTML.

Isso também tornou possível separar o estudo da automação do
comportamento específico de uma plataforma externa.    

## 🛠️ Conceitos estudados durante o projeto
-Seletores CSS;
 -DOM;
 -Selenium;
 -WebDriver;
 -automação de navegador;
 -WebDriverWait;
 -eventos e entrada de teclado;
 -manipulação de elementos HTML;
 -medição de tempo;
 -cálculo de WPM;
 -debugging de automações.

# 👨‍💻 Autor
<img src="./assets/FotoReadme.png" width="250" style="border-radius: 10px; display: block; clear: both; margin-bottom: 15px;">

**Jorge Enrique** - Programador Objetivo e Profissional.