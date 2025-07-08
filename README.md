
# 📦 Sistema de Gerenciamento de Mercado

Este projeto eu comecei desenvolvendo ele em modo **console**, e agora evoluir criando uma página utilizando **Streamlit**. Ele utiliza o **Firebase Realtime Database** como backend. Com ele, você pode:

- Adicionar e editar produtos
- Registrar vendas
- Visualizar listas de vendas e produtos
- Deletar registros

## 🚀 Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Firebase Realtime Database](https://firebase.google.com/products/realtime-database)
- [Requests](https://docs.python-requests.org/)

## 📂 Funcionalidades

- **Adicionar Venda**
- **Adicionar Produto**
- **Editar Venda**
- **Editar Produto**
- **Listar Vendas e Produtos**
- **Deletar Venda**
- **Deletar Produto**

## 🛠️ Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/guilhermetrutaa/Front-CrudPython-Firebase.git
cd Front-CrudPython-Firebase
```

2. Instale as dependências:

```bash
pip install streamlit
pip install requests
```

3. Altere a variável `link` com a URL da sua instância do Firebase:

```python
link = "https://seu-projeto.firebaseio.com/"
```

4. Rode o projeto com:

```bash
streamlit run nome_do_arquivo.py
```

## 📝 Requisitos

- Python 3.7+
- Conta no Firebase com um Realtime Database criado

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
