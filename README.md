# APIs

Projeto destinado a apresentar 3 exemplos de APIs (Application Programming Interface) com suas descriçoes e uma breve demonstração do uso.

## 1. Vagalume API

#### Descrição:
Na API do Vagalume é gratuita e com ela é possivel especificar o artista e a musica a ser buscada, imprimir a letra da música, fazer a tradução da letra para o português e listar todas as músicas do artista entre outras funcionalidades. 

#### Demonstração:
*Requisição:*
```
jQuery.getJSON(
    "https://www.vagalume.com.br/u2/index.js",
    function (data) {
        // Nome do artista
        alert(data.artist.desc);
    }
);
```

*Resposta:*

```
{
    "artist":{
        "id":"3ade68b2g3b86eda3",
        "desc":"U2",
        "url":"/u2/",
        "pic_small":"/u2/images/profile.jpg",
        "pic_medium":"/u2/images/u2.jpg",
        "rank":{
            "pos":"102",
            "period":201110,
            "views":"284526",
            "uniques":"112363",
            "points":"17.1"
        },
        "genre":
            [
                {
                    "name":"Rock Alternativo",
                    "url":"/browse/style/rock-alternativo.html"
                },{
                    "name":"Rock",
                    "url":"/browse/style/rock.html"
                },
                ...
            ],
        "related":
            [
                {
                    "id":"3ade68b5ge177eda3",
                    "name":"Pearl Jam",
                    "url":"/pearl-jam/"
                },{
                    "id":"3ade68b5g1bf7eda3",
                    "name":"Queen",
                    "url":"/queen/"
                },
                ...
            ],
        "toplyrics":{
            "item":
                [
                    {
                        "id":"3ade68b6gc1d8fda3",
                        "desc":"With Or Without You (tradu\u00e7\u00e3o)",
                        "url":"/u2/with-or-without-you-traducao.html"
                    },{
                        "id":"3ade68b3gdb86eda3",
                        "desc":"One",
                        "url":"/u2/one.html"
                    },
                    ...
                ]
        },
        "albums":{
            "item":
                [
                    {
                        "id":"3ade68b6g4f38fda3",
                        "desc":"No line on the horizon",
                        "url":"/u2/discografia/no-line-on-the-horizon.html",
                        "year":"2009",
                        "label":"Island/Universal"
                    },{
                        "id":"3ade68b6ge7e7fda3",
                        "desc":"U218 Singles",
                        "url":"/u2/discografia/u218-singles.html",
                        "year":"2006",
                        "label":"Island/Polygram"
                    },
                    ...
                ]
        }
    }
}
```
## 2. Foursquare API

#### Descrição:

O Foursquare é um serviço social de local que permite que os usuários explorem o mundo ao seu redor. A API do Foursquare permite que os desenvolvedores de aplicativos interajam com a plataforma Foursquare dando acesso ao seu banco de dados e fornecendo interação com os usuários e comerciantes da plataforma. 

#### Demonstração:
*Requisição:*

```
#Autenticação do usuário
Https://foursquare.com/oauth2/authenticate
    ? Client_id = YOUR_CLIENT_ID
    & Response_type = código
    & Redirect_uri = YOUR_REGISTERED_REDIRECT_URI
                  
#Se o usuário aceitar, eles serão redirecionados de volta para
    Https: // YOUR_REGISTERED_REDIRECT_URI /? Code = CODE
                  
#Seu servidor deve trocar o código que obteve para um token de acesso. Faça um pedido para
Https://foursquare.com/oauth2/access_token
    ? Client_id = YOUR_CLIENT_ID
    & Client_secret = YOUR_CLIENT_SECRET
    & Grant_type = license_code
    & Redirect_uri = YOUR_REGISTERED_REDIRECT_URI
    & Code = CODE
                  
```

*Resposta:*

```
{Access_token: ACCESS_TOKEN}
```

## 3. Vimeo API

#### Descrição:




