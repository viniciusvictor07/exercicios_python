import urllib.request

def acessar(site):
    print(f"Acessando o site {site}...")
    try:
        conexao = urllib.request.urlopen('http://www.pudim.com.br')
        return f"Site {site} acessado com sucesso!"
    
    except:
        return f"Erro ao acessar o site {site}."