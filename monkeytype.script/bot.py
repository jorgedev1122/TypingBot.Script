from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from pathlib import Path


# =========================================================
# CONFIGURAÇÃO
# =========================================================

INTERVALO = 0.01


# =========================================================
# INICIAR
# =========================================================

print("Iniciando bot...")

driver = webdriver.Chrome()

driver.get("https://monkeytype.com/")

print("Monkeytype carregado!")


# =========================================================
# COOKIES
# =========================================================

try:
    botao_cookies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'accept all')]")
        )
    )

    botao_cookies.click()

    print("Cookies aceitos!")

except:
    print("Cookies não apareceram.")


# =========================================================
# PEGAR PALAVRAS DO MONKEYTYPE
# =========================================================

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


# =========================================================
# CRIAR FRASE
# =========================================================

frase = " ".join(palavras)

print()
print("================================")
print("FRASE")
print("================================")
print(frase)

print()
print(f"Palavras: {len(palavras)}")
print(f"Caracteres: {len(frase)}")


# =========================================================
# ABRIR LABORATÓRIO
# =========================================================

arquivo = Path(__file__).parent / "teste.html"

driver.get(arquivo.resolve().as_uri())

print()
print("Laboratório aberto!")


# =========================================================
# COLOCAR FRASE
# =========================================================

texto = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "texto")
    )
)

driver.execute_script(
    """
    arguments[0].textContent = arguments[1];
    """,
    texto,
    frase
)


# =========================================================
# CAMPO
# =========================================================

campo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "entrada")
    )
)

print("Campo encontrado!")


# =========================================================
# PREPARAÇÃO
# =========================================================

print()
print("================================")
print("MOTOR DE DIGITAÇÃO")
print("================================")

print(f"Intervalo: {INTERVALO}s")
print(f"Palavras: {len(palavras)}")

input("Pressione ENTER para começar...")


# =========================================================
# MOTOR
# =========================================================

campo.click()

inicio = time.perf_counter()

erros = 0
corretos = 0

indice = 0


for palavra in palavras:

    print(f"\rDigitando: {palavra:<20}", end="")

    # -----------------------------------------------------
    # DIGITAR CADA CARACTERE
    # -----------------------------------------------------

    for caractere in palavra:

        campo.send_keys(caractere)

        corretos += 1

        time.sleep(INTERVALO)

    # -----------------------------------------------------
    # ESPAÇO ENTRE PALAVRAS
    # -----------------------------------------------------

    campo.send_keys(" ")

    time.sleep(INTERVALO)

    indice += 1


fim = time.perf_counter()


# =========================================================
# RESULTADOS
# =========================================================

tempo = fim - inicio

total_caracteres = len(frase)

total_palavras = len(palavras)


# WPM padrão:
# 5 caracteres = 1 palavra

wpm = (
    total_caracteres / 5
) / (
    tempo / 60
)


precisao = (
    corretos / (corretos + erros) * 100
    if corretos + erros > 0
    else 100
)


# =========================================================
# MOSTRAR
# =========================================================

print()
print()
print("================================")
print("RESULTADO")
print("================================")

print(f"Palavras:   {total_palavras}")
print(f"Caracteres: {total_caracteres}")
print(f"Tempo:      {tempo:.3f}s")
print(f"WPM:        {wpm:.2f}")
print(f"Precisão:   {precisao:.2f}%")
print(f"Erros:      {erros}")


# =========================================================
# MOSTRAR NA PÁGINA
# =========================================================

resultado = driver.find_element(
    By.ID,
    "resultado"
)

driver.execute_script(
    """
    arguments[0].innerHTML = `
        <strong>RESULTADO</strong><br><br>

        WPM: ${arguments[1]}<br>
        Precisão: ${arguments[2]}%<br>
        Erros: ${arguments[3]}<br>
        Tempo: ${arguments[4]}s
    `;
    """,
    resultado,
    f"{wpm:.2f}",
    f"{precisao:.2f}",
    erros,
    f"{tempo:.3f}"
)


print()
print("Teste concluído!")

input("Pressione ENTER para fechar...")

driver.quit()