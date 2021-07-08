# Estudando RestFramework pela documentaçao oficial.

- O meu objetivo e tentar ler o maximo da documentação do framework e aprender mais sobre APIs e padrão REST.

- O codigo será no padrão ingles, porem os comentarios e esse
README.md ficara em portugues para melhor compreensão.
  
- Pode apresentar erros de entendimento.

## TOPICO BASICO 1: Serializaçao
Serializar e o mesmo que apresentar um dado de uma forma diferente da que ele foi criado.
No contexto de apis, apresentar os valores do modelo que esta no banco de dados na forma de um json (que e o padrão de apis).

O rest framework da algumas opções de como realizar essa tarefa.

- 1º Criar a pasta serializers.py dentro do app.
- 2º Importar ``from rest_framework import serializers`` e os modelos.
- 3º Para saber como e a estrutura veja o arquivo ``api_test/serializers.py``

Nesse metodo apresentado no começo do codigo de serializers.py segue o padrão:
- As primeiras linhas de codigo define os campos que serão serializados (nem todos precisão ser serializados).
- Os metodos create() e update() definem como as instancias serão criadas e atualizadas nessa sequencia.
- Essa e a forma explicita de criar um serializer.
- Atenção que os dados gerados são um dicionario python e não um json
- Para json, JSONRenderer().render(serializer.data)

Não entrarei no merito da desserialização. 
- Se tiver curiosidade: https://www.django-rest-framework.org/tutorial/1-serialization/

Usando ModelSerializers:
E a forma mais facil de tratar serializers.
Estrutura:
```
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity_in_stock']
```

dica da documentação: No shell e possivel verificar o serializador
```
from api_test.serializers import ProductSerializer
serializer = ProductSerializer()
print(repr(serializer))
```

Agora trabalhando um pouco com a view para que esse dados sejam apresentados. `api_test/views.py`
Sem usar os recursos do rest_framework, apenas com django. Ficara no final do arquivo comentado.

DICA: Usar httpie para testar.

## TOPICO BASICO 2: Requests e Responses (solicitações e respostas)
Imagine que requests são os dados enviados de você(cliente) para o web(servidor)
E o reponse é como se fosse a reposta que o servidor manda de volta, dizendo se a operação foi um sucesso ou falhou. 
Para saber mais: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

No restframework o objeto request estende HttpRequest 
O request.data lida com dados arbritarios. Trabalha com Post, Put e Patch methods.

Os codigos de status são tratos de forma mais visual em vez de serem diretos. Por exemplo:
`HTTP_400_BAD_REQUEST` que vem da biblioteca status.

Caso queira usar a view do rest existem duas possibilidades:
- @api_view para trabalhar com funções
- APIView para lidar com classes

A vantagem neles e que possuem algumas formas de tratar os dados e possuem excessoes do tipo ParseError, Bad Request.

## TOPICO BASICO 3: Autenticação e permissões

O modulo de permissão padrão do rest pode ser importado `from rest_framework import permissions`

Deve ser adicionado o seguinte codigo na view para que exista as permissões: `permission_classes = [permissions.IsAuthenticatedOrReadOnly]`
So ira funcionar se estiver usado APIView para criar as views. Se estiver usando @api_view a abordagem tera que ser outra.

Adicionando `path('api-auth/', include('rest_framework.urls'))` nas rotas o rest fornece um formulario de 
autenticação padrão.

Criando permissões personalizadas:
- Criando o arquivo permissions.py no app que deseja criar as proprias permissões.
- Importando o `from rest_framework import permissions`
- A classe deve estender a classe `permissions.BasePermission` ou outra classe de permissão.
- Olhe o arquivo `permissions.py` para ver a estrutura.
- As novas permissões podem ser adicionadas na variavel `permission_classes` na views.


## TOPICO BASICO 4: ViewSet

ViewSets são otimos para agilizar o desenvolvimento das views. Apresentam pouco codigo e permite que com 
apenas algumas variaveis configurem a visualização. Ainda deixam a complexidade de criar rotas de lado. 
Gerando automaticamente a partir de um Router. Ela ja realiza 'Retrieve' e 'List', acabando com o codigo duplicado.

- Exemplo de uso na classe UserViewSet em views.py
- Olhe urls.py para ver como se faz uso do roteador.


# Avançando no framework:

## TOPICO AVANÇADO 1: Views

O Rest framework oferece diversas classes de views para nos ajudar na hora de criar a visualização.
A APIView e baseada na classe View do django, diferente do django que lida com requests utilizando 
HttpResponse APIView com o objeto`Request` que facilita o desenvolvimento.
Da mesma maneira que os requests os responses tambem possuem seu proprio objeto `Response`.

A APIView possui as variaveis `authentication_classes` e `permission_classes` que permitem gerenciar de forma
facil a segurança da api.

Possui os metodos principais get() e post() para realizar as operações da api, que devem ser escritos explicitamente.

Existem alguns atributos e metodos menos comuns, mas bem valiosos:
- renderer_classes: Configura o renderizador que sera usado.
- parse_classe: Configura o tipo de parser
- throttle_classes: define o controlador da taxa da API. Muito parecido com permission_classes
- check_permissions(self, request): Verifica a permissão. 
Os outros metodos e atributos podem ser vistos na documentação: https://www.cdrf.co/


As visualizações baseadas em funções usam a assinatura: `@api_view(['GET', 'POST'])`.
Uma forma limpa de criar as funções de forma explicita.
Porém deve ser mais facil utilizar as views do modulo generics.

Generic views: # TODO

A forma mais facil e mais aconcelhada na maioria dos casos e usando a classe ViewSet do modulo viewset.
Nela a configuração da api e simples e clara deixando facil de ser configurado.

Para mais informações sobre views: https://www.cdrf.co/

