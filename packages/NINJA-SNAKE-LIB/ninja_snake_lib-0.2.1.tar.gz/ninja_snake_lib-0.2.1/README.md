# Ninja Snake Lib

Biblioteca python para projetos que utilizam o Django framework.

### Motivação

Devido aos projetos compartilharem os mesmos trechos de código nas configurações dos sistemas,
foi criada essa biblioteca para melhorar a reutilização e a manutenção do código nesses sistemas.

### Dependências

Está biblioteca possui a dependência do Django Framework **>= 3.1.6**.

### Funcionalidades

- ReadDotenv
- JSONFormatter
- validate_external_api_key
- validate_sns_subscription
- gn_context_correlation_id_from_request
- CustomisedJSONFormatter
- gn_py_tracker

### Instalação

`pip install ninja-snake-lib`

### Read Dotenv

O módulo **ReadDotenv** tem a função de ler as variáveis de ambiente contidas
no arquivo **.env** e criá-las no sistema operacional.

**Como Utilizar**

No início do arquivo settings.py de ser feito o import do módulo.

`from ninja-snake-lib.read_dotenv import ReadDotenv`

Deve ser passado como parâmetro o path onde se encontra o arquivo **.env**.

`ReadDotenv.read_dotenv(Path(__file__).resolve().parent)`

### JSONFormatter

O módulo **JSONFormatter** tem a função de formatar a saída do log.

**Como Utilizar**

Para utilizar o módulo, basta fazer a chamada na config do LOG como no exemplo
abaixo:

##### Config do log no settings.py
```
 LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': 'ninja_snake_lib.json_formatter.JSONFormatter'
            }
        },
        ...
```

### gn_context_correlation_id_from_request

Decorator que gera correlation_id para os logs dos requests



### CustomisedJSONFormatter

O módulo **CustomisedJSONFormatter** implementa um formatador padronizado para as entradas de log
nos sistemas Django.

Para utilizar, adicionar em settings.py:

```
from ninja_snake_lib import CustomisedJSONFormatter
from ninja_snake_lib.setup_correlation_id import ContextFilter

...
ch = logging.StreamHandler()
ch.setFormatter(CustomisedJSONFormatter())

LOGGER.addHandler(ch)
LOGGER.addFilter(ContextFilter())
```


## Decorators

### validate_external_api_key

O decorator **validate_external_api_key** tem a função de validar o parâmetro
**HTTP_AUTHORIZATION** no header das requisições recebidas.

**Como Utilizar**

No início do arquivo da view que irá utilizar o decorator, fazer o import do mesmo.

`from ninja_snake_lib.decorators import validate_external_api_key`

Com o decorator importado, podemos fazer uso dele como no exemplo abaixo:

```
@validate_external_api_key
def teste_decorator(x):
    return x * 3
```

### validate_sns_subscription

O decorator **validate_sns_subscription** tem a função de validar o parâmetro
**HTTP_X_AMZ_SNS_MESSAGE_TYPE** no header das requisições recebidas.

**Como Utilizar**

No início do arquivo da view que irá utilizar o decorator, fazer o import do mesmo.

`from ninja_snake_lib.decorators import validate_sns_subscription`

Com o decorator importado, podemos fazer uso dele como no exemplo abaixo:

```
@validate_sns_subscription
def teste_decorator(x):
    return x * 3
```

## gn_py_tracker

Biblioteca para tracker de eventos de uma aplicação.

### Como Utilizar

Está lib pode ser usada em qualquer sistema python.

Devemos fazer o seguinte import do módulo.

`from gn_py_tracker.tracker import Tracker`

Para inicializar o tracker deve ser passado como parâmetro o "tracker_type" e parâmetros adicionais
de acordo com o tipo do tracker.

`tracker = Tracker.create_tracker(tracker_type="file")`

Para envio do evento devemos chamar o método "send_event"

`tracker.send_event(event)`

### Configuração adicional

Passar como parâmetro o logger do sistema que estamos importando o pacote, da seguinte forma:

`tracker = Tracker.create_tracker(tracker_type="file", app_logger=logger)`

OBS: Para uso em sistemas Django devemos instanciar o tracker após a definição do logger usado no projeto
e após a definição de "LANGUAGE_CODE" e "TIME_ZONE" para correta configuração do logger.

## Testes

Para rodar os testes devemos instalar as dependências para o teste unitário
com o comando abaixo:

`pip install -r requirements.txt`

Para rodar os testes devemos estar no diretório root do projeto e executar o
comando abaixo:

`python -m unittest`

> Podemos também utilizar o parâmetro -v (verbose) para exibir os nomes nos testes
> que rodaram.

##### Exemplo

`python -m unittest -v`
