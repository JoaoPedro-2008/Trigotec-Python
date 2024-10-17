import math

def calcular_trigonometria(cateto_oposto, cateto_adjacente):
    # Calcula a hipotenusa usando o Teorema de Pitágoras
    hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
    
    # Calcula seno, cosseno e tangente
    seno = cateto_oposto / hipotenusa
    cosseno = cateto_adjacente / hipotenusa
    tangente = cateto_oposto / cateto_adjacente if cateto_adjacente != 0 else "Indefinido"
    
    # Calcula o ângulo usando a função arco seno
    angulo = math.degrees(math.asin(seno))  # ângulo correspondente ao cateto oposto

    return seno, cosseno, tangente, angulo

# Exemplo de uso
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

seno, cosseno, tangente, angulo = calcular_trigonometria(cateto_oposto, cateto_adjacente)

print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente}")
print(f"Ângulo correspondente: {angulo:.2f} graus")
