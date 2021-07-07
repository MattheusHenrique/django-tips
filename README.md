# Estudando RestFramework pela documentaçao oficial.

- O meu objetivo e tentar ler o maximo da documentação do framework e aprender mais sobre APIs e padrão REST.

- O codigo será no padrão ingles, porem os comentarios e esse
README.md ficara em portugues para melhor compreensão.
  
- Pode apresentar erros de entendimento.

## TOPICO 1: Serializaçao
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

## TOPICO 2: Requests e Responses (solicitações e respostas)
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

## TOPICO 3: Autenticação e permissões

