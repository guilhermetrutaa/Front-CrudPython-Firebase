import streamlit as st
import requests
import json

link = "https://crudfirebase-4c3cf-default-rtdb.firebaseio.com/"

st.title("📦 Sistema de Gerenciamento de Mercado")

menu = st.sidebar.selectbox("Menu", [
    "Adicionar Venda",
    "Adicionar Produto",
    "Editar Venda",
    "Editar Produto",
    "Listar Vendas e Produtos",
    "Deletar Venda",
    "Deletar Produto"
])

def post_firebase(path, data):
    return requests.post(f'{link}/{path}/.json', data=json.dumps(data))

def patch_firebase(path, data):
    return requests.patch(f'{link}/{path}/.json', data=json.dumps(data))

def get_firebase(path=""):
    return requests.patch(f'{link}/{path}/.json')

def delete_firebase(path):
    return requests.delete(f'{link}/{path}/.json')

if menu == "Adicionar Venda":
    st.subheader("📑 Adicionar Venda")
    cliente = st.text_input("Nome do Cliente: ")
    produto = st.text_input("Nome do Produto: ")
    preco = st.number_input("Preço do Produto (R$): ", min_value=0.0, step=0.01)

    if st.button("Salvar Venda"):
        dados = {'cliente': cliente, 'produto': produto, 'preco': preco}
        requisicao = post_firebase("Vendas", dados)
        st.success("Venda Registrada com sucesso!")
        st.json(requisicao.json())

if menu == "Adicionar Produto":
    st.subheader("🛒 Adicionar Produto")
    nome = st.text_input("Nome do Produto: ")
    preco = st.number_input("Preço do Produto (R$): ", min_value=0.0, step=0.01)
    quantidade = st.text_input("Quantidade do Produto:")

    if st.button("Salvar Produto"):
        dados = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
        requisicao = post_firebase("Produtos", dados)
        st.success("Produto Registrado com sucesso!")
        st.json(requisicao.json())

if menu == "Editar Venda":
    st.subheader("📝 Editar Venda")
    id_venda = st.text_input("ID da Venda")
    campo = st.selectbox("Campo que deseja editar", ["cliente", "produto", "preco"])
    novo_valor = st.text_input(f"Novo valor para '{campo}'")

    if st.button("Atualizar Venda"):
        requisicao = patch_firebase(f"Vendas/{id_venda}", {campo: novo_valor})
        st.success("Venda atualizada com sucesso!")
        st.json(requisicao.json())

if menu == "Editar Produto":
    st.subheader("✏️ Editar Produto")
    id_produto = st.text_input("ID do Produto")
    campo = st.selectbox("Compo que deseja editar", ["nome", "preco", "quantidade"])
    novo_valor = st.text_input(f"Novo valor para '{campo}'")

    if st.button("Atualizar Produto"):
        requisicao = patch_firebase(f"Produtos/{id_produto}", {campo: novo_valor})
        st.success("Produto atualizadop com sucesso!")
        st.json(requisicao.json())

if menu == "Listar Vendas e Produtos":
    st.subheader("📋 Vendas e Produtos")

    if st.button("Carregar Dados"):
        requisicao = get_firebase()
        dados = requisicao.json()

        st.subheader("📑 Vendas")
        st.json(dados.get("Vendas", {}))

        st.subheader("🛒 Produtos")
        st.json(dados.get("Produtos", {}))

if menu == "Deletar Venda":
    st.subheader("🗑️ Deletar Venda")

    id_venda = st.text_input("Id da Venda")

    if st.button("Deletar Venda"):
        requisicao = delete_firebase(f"Vendas/{id_venda}")
        st.success("Venda deletada com sucesso!")
        st.json(requisicao.json())

if menu == "Deletar Produto":
    st.subheader("🗑️ Deletar Produto")

    id_produto = st.text_input("Id do Produto")

    if st.button("Deletar Produto"):
        requisicao = delete_firebase(f"Produtos/{id_produto}")
        st.success("Produto deletado com sucesso!")
        st.json(requisicao.json())
