# Trabalho 2 de Redes de Computadores 2

Repositório contendo as implementações práticas de programação em redes de computadores desenvolvidas para a disciplina do Prof. Alessandro Vivas Andrade. 

O projeto explora a comunicação cliente-servidor utilizando os protocolos TCP e UDP, manipulação de threads, criação de um sistema de chat bidirecional e análise de pacotes de rede.

## 👥 Autores
* Lucas Rocha Oliveira
* Luiz Felipe Melo Oliveira
* Luiz Guilherme Oliveira Pires
* Otávio Gomes Calazans

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Sistema Operacional:** Desenvolvido e testado em ambiente Linux (Ubuntu)
* **Bibliotecas:** `socket`, `threading`, `asyncio`, `websockets`
* **Ferramenta de Análise:** Wireshark

## 📂 Estrutura do Repositório

O código-fonte está organizado em diretórios separados para cada exercício:

* **Exercício 1 (Cliente-Servidor TCP):** Comunicação básica TCP com envio de mensagens e confirmação de recebimento.
* **Exercício 2 (Servidor Echo UDP):** Implementação de um serviço de eco validando o tamanho máximo da mensagem em UDP (64 KB).
* **Exercício 3 (Chat em Rede TCP):** Sistema de chat bidirecional em tempo real utilizando threads para comunicação paralela.
* **Exercício 4 (Servidor de Hora com Threads):** Servidor TCP multithread que atende múltiplas solicitações simultâneas para fornecer a hora atual com geração de logs.
* **Exercícios 5 a 9 (Análise com Wireshark):** Logs e capturas de tráfego referentes a requisições HTTP, handshake TCP, consultas DNS, protocolo ICMP (ping) e DHCP.
* **Exercício 10 (Chat WebSocket):** Sistema de chat moderno em tempo real implementado via WebSockets no Linux.

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de estar utilizando um ambiente Linux com o Python 3.10 ou superior instalado.

### Instalação

1. Clone o repositório para a sua máquina local:
```bash
git clone [https://github.com/Lucas-Rocha-Oliveira/Trabalho-2-Redes-2.git](https://github.com/Lucas-Rocha-Oliveira/Trabalho-2-Redes-2.git)
cd Trabalho-2-Redes-2