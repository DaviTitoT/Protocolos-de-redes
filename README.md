# HTTP Performance Study

Estudo comparativo do protocolo **HTTP** em um cenário realista de desenvolvimento de sistemas, avaliando seu desempenho e sua adequação em relação a outras alternativas de comunicação.


##  Sobre o projeto

Este projeto foi desenvolvido com o objetivo de demonstrar, por meio de um cenário prático, por que o protocolo **HTTP** continua sendo a melhor escolha para diversas aplicações distribuídas modernas.

Além de apresentar uma fundamentação teórica, o projeto inclui um **benchmark em Python** para comparar o comportamento do HTTP com outros mecanismos de comunicação, analisando aspectos como desempenho, confiabilidade e facilidade de integração.


##  Objetivo

Avaliar diferentes formas de comunicação entre sistemas e demonstrar, através de experimentos, em quais situações o protocolo HTTP apresenta a melhor relação entre:

* desempenho;
* confiabilidade;
* interoperabilidade;
* facilidade de desenvolvimento;
* escalabilidade;
* suporte pelas tecnologias atuais.



##  Cenário proposto

Foi considerado o desenvolvimento de um **sistema hospitalar distribuído**, onde diferentes serviços precisam trocar informações em tempo real, como:

* cadastro de pacientes;
* consulta de prontuários;
* registro de exames;
* agendamento de consultas;
* autenticação de usuários.

Nesse cenário, diversos clientes (navegadores, aplicativos móveis e outros sistemas) precisam acessar uma API de forma segura e confiável.

Embora existam protocolos potencialmente mais rápidos em situações específicas, o HTTP oferece um equilíbrio muito superior entre desempenho, simplicidade, compatibilidade e facilidade de manutenção.



##  Protocolos comparados

O estudo realiza uma comparação entre:

* HTTP
* TCP Socket
* UDP
* Comunicação baseada em filas (conceitualmente)

Foram analisados critérios como:

* tempo de resposta;
* facilidade de implementação;
* confiabilidade;
* garantia de entrega;
* interoperabilidade;
* suporte em navegadores;
* segurança;
* escalabilidade.



##  Benchmark

O notebook realiza testes locais simulando múltiplas requisições HTTP.

São coletadas métricas como:

* tempo total de execução;
* tempo médio por requisição;
* throughput;
* quantidade de requisições processadas.

Os resultados servem como base para justificar tecnicamente a utilização do HTTP no cenário apresentado.



##  Tecnologias utilizadas

* Python 3
* Flask
* Requests
* Time
* Threading
* Jupyter Notebook



##  Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/http-performance-study.git

cd http-performance-study
```

### 2. Instale as dependências

```bash
pip install flask requests notebook
```

### 3. Execute o notebook

```bash
jupyter notebook
```

Abra o arquivo:

```
comparacao_http_protocolos.ipynb
```

e execute todas as células.



##  Resultados esperados

Os experimentos mostram que:

* o HTTP apresenta excelente desempenho para aplicações cliente-servidor;
* sua sobrecarga é pequena quando comparada aos benefícios oferecidos;
* sua padronização facilita integrações entre diferentes linguagens e plataformas;
* recursos como HTTPS, autenticação, cache e APIs REST tornam sua adoção a opção mais prática para aplicações modernas.



##  Conclusão

Embora existam protocolos especializados para cenários específicos, como streaming contínuo, jogos online ou sistemas embarcados, o HTTP continua sendo a escolha mais equilibrada para a maioria das aplicações distribuídas.

Sua ampla adoção pela indústria, facilidade de integração, suporte nativo em praticamente todas as plataformas e excelente relação entre desempenho e confiabilidade justificam sua utilização como protocolo principal em sistemas web modernos.



##  Autor

Desenvolvido como projeto de estudo sobre protocolos de comunicação em redes de computadores e avaliação de desempenho do protocolo HTTP.
