import streamlit as st

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

# Streamlit App
st.title("Sieb des Eratosthenes")
st.write("Geben Sie eine Obergrenze n ein, um die Primzahlen bis n zu finden:")

# Eingabefeld für die Obergrenze
n = st.number_input("Obergrenze n:", min_value=2, value=10)

if st.button("Primzahlen finden"):
    prime_numbers = sieve_of_eratosthenes(n)
    st.write(f"Die Primzahlen bis {n} sind: {prime_numbers}")