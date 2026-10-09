# Lista de compras

Aplicação de lista de compras com:

- **Frontend:** HTML, CSS e JavaScript puro;
- **Backend:** Python com FastAPI;
- **Servidor:** Uvicorn;
- **API:** rotas para listar, criar, editar e excluir itens.

O frontend é servido pelo próprio FastAPI. Portanto, frontend e backend são
executados juntos na mesma porta.

## Estrutura do projeto

```text
Shopping_list_api/
├── controllers/
│   └── itensControllers.py
├── data/
│   ├── itens.py
│   └── schema.py
├── frontend/
│   └── index.html
├── middlewares/
│   └── log_middleware.py
├── routes/
│   └── itensRoutes.py
├── main.py
├── requirements.txt
├── run.py
└── run.pyw
```

## Requisitos

- Windows 10 ou Windows 11;
- Python 3.10 ou superior;
- PowerShell.

Verifique o Python com:

```powershell
py --version
```

## Instalação no Windows

Abra o PowerShell na pasta do projeto:

```powershell
Set-Location "C:\Users\joaop\OneDrive\Desktop\Shopping_list_api"
```

Crie um ambiente virtual:

```powershell
py -m venv .venv
```

Instale as dependências usando o Python do ambiente virtual. Esta forma evita
problemas de bloqueio do arquivo `pip.exe`:

```powershell
.\.venv\Scripts\python.exe -m pip install -r .\requirements.txt
```

## Executar com terminal visível

Use esta opção durante o desenvolvimento, pois os erros aparecem no terminal:

```powershell
.\.venv\Scripts\python.exe .\run.py
```

Depois abra:

<http://127.0.0.1:8000/>

Para parar o servidor, pressione `Ctrl + C`.

## Executar sem abrir o terminal

O arquivo `run.pyw` inicia o servidor sem mostrar uma janela do PowerShell.

Pelo PowerShell:

```powershell
.\.venv\Scripts\pythonw.exe .\run.pyw
```

Também é possível dar duplo clique em `run.pyw` no Explorador de Arquivos.

Para parar a API executada com `pythonw.exe`, finalize o processo `pythonw.exe`
no Gerenciador de Tarefas.

Durante o desenvolvimento, prefira `run.py`, porque o `run.pyw` não mostra as
mensagens de erro.

## URLs disponíveis

| Recurso | URL |
|---|---|
| Frontend | <http://127.0.0.1:8000/> |
| Listar itens | <http://127.0.0.1:8000/shopping/> |
| Documentação Swagger | <http://127.0.0.1:8000/docs> |
| Especificação OpenAPI | <http://127.0.0.1:8000/openapi.json> |

## Rotas da API

| Método | Rota | Função |
|---|---|---|
| `GET` | `/shopping/` | Lista todos os itens |
| `GET` | `/shopping/{id}` | Busca um item |
| `POST` | `/shopping/` | Cria um item |
| `PATCH` | `/shopping/{id}` | Atualiza um item |
| `DELETE` | `/shopping/{id}` | Remove um item |

Exemplo para criar um item:

```powershell
curl.exe -X POST http://127.0.0.1:8000/shopping/ `
  -H "Content-Type: application/json" `
  -d '{"nome":"Leite","quantidade":2,"valor":5.50}'
```

## Observações

- Os dados ficam armazenados em memória e são perdidos quando o servidor é
  reiniciado.
- O frontend usa a URL relativa `/shopping`, por isso não precisa configurar
  manualmente o endereço do backend.
- Se a porta `8000` estiver ocupada, encerre o processo que a utiliza ou altere
  a porta em `run.py` e `run.pyw`.
- O aviso `WatchFiles detected changes in .venv` é evitado mantendo
  `reload=False` nos arquivos de execução.
