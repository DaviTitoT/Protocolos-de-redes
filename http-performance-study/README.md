# HTTP Performance Study

## Descrição
Este projeto tem como objetivo demonstrar, por meio de um cenário realista e benchmarks em Python, por que o protocolo HTTP é uma escolha adequada para sistemas distribuídos em contexto hospitalar, comparando-o com TCP.

## Objetivo
Avaliar o comportamento de requisições HTTP e TCP em cenários de comunicação entre módulos de um sistema hospitalar, considerando simplicidade de implementação, interoperabilidade, rastreabilidade e desempenho prático.

## Cenário
O estudo simula um ambiente em que um cliente envia solicitações para um serviço de integração hospitalar. O foco é observar o tempo de resposta e a viabilidade de uso em um ambiente realista, sem depender de uma infraestrutura complexa.

## Tecnologias
- Python 3
- Flask
- Requests
- Matplotlib
- Pandas
- Jupyter Notebook

## Estrutura do projeto
- docs/: notebook com introdução, fundamentação, metodologia e análise parcial.
- src/: implementações de servidores e clientes HTTP/TCP, além do benchmark.
- data/: arquivos CSV e imagens geradas pelos testes.

## Instruções de execução
1. Entre na pasta do projeto.
2. Crie um ambiente virtual e instale as dependências:
   - `python -m venv .venv`
   - `.venv\Scripts\activate`
   - `python -m pip install -r requirements.txt`
3. Execute o benchmark completo:
   - `python src/benchmark.py`
4. Para testes manuais:
   - HTTP: `python src/server_http.py --port 8001` e `python src/client_http.py`
   - TCP: `python src/server_tcp.py --port 9001` e `python src/client_tcp.py`

## Resultados parciais
Os benchmarks geram um arquivo CSV em `data/resultados.csv`, um gráfico em `data/benchmark_http_tcp.png` e um resumo estatístico em `data/summary.csv`.

## Status atual
- Progresso aproximado: 70%.
- Concluído: benchmark HTTP e TCP, documentação parcial, estrutura do projeto e geração automática de gráficos.
- Em andamento: análise final, benchmark UDP e conclusão do notebook.

## Próximas etapas
- ampliar a análise com benchmark UDP;
- incluir mais métricas, como taxa de sucesso e variabilidade;
- documentar a análise parcial no notebook e finalizar a seção de conclusão e referências.
