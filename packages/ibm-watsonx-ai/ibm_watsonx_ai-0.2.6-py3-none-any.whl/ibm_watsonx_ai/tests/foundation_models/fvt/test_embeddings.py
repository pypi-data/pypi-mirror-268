#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------
import pytest

from ibm_watsonx_ai.foundation_models import Embeddings
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames as EmbedParams
from ibm_watsonx_ai.foundation_models.utils import get_embedding_model_specs

from ibm_watsonx_ai.tests.utils.utils import get_wml_credentials

credentials = get_wml_credentials()
available_models = [el.get('model_id') for el in get_embedding_model_specs(credentials.get('url')).get('resources')]


class TestTextEmbeddings:
    """
    This tests covers:
    - Embeddings generate with and without params
    - Embeddings embed_documents (texts)
    - Embeddings embed_query
    - Serialisation: to_dict and from_dict methods
    """
    inputs = ['What is a generative ai?', 
              'What is a loan and how does it works?']
    
    @pytest.mark.parametrize('model', available_models )
    def test_01a_generate_emebdding(self, model, api_client, project_id):
        embedding = Embeddings(model_id=model,
                               api_client=api_client,
                               project_id=project_id)
        
        generate_embedding = embedding.generate(inputs=TestTextEmbeddings.inputs)

        assert generate_embedding.get('model_id') == model, 'Incorrect model in response'

        assert len(generate_embedding.get('results', [])) == len(TestTextEmbeddings.inputs), \
            f"{len(TestTextEmbeddings.inputs)} inputs were given but only {len(TestTextEmbeddings.inputs)} vectors got"

        assert all(isinstance(el, float) for el in generate_embedding.get('results', [{}])[0].get('embedding')), \
            'Not all embedding vector elements are floats'
        
    @pytest.mark.parametrize('model', available_models )
    def test_01b_generate_emebdding_more_than_limit(self, model, api_client, project_id):
        max_input_tokens = 3
        embed_params = {
            EmbedParams.TRUNCATE_INPUT_TOKENS: max_input_tokens,
        }
        embedding = Embeddings(model_id=model,
                               api_client=api_client,
                               project_id=project_id,
                               params=embed_params)
        
        long_inputs = TestTextEmbeddings.inputs[:1]*21
        generate_embedding = embedding.generate(inputs=long_inputs)

        assert generate_embedding.get('model_id') == model, 'Incorrect model in response'

        assert len(generate_embedding.get('results', [])) == len(long_inputs), \
            f"{len(TestTextEmbeddings.inputs)} inputs were given but only {len(long_inputs)} vectors got"

        assert generate_embedding.get('input_token_count') == max_input_tokens*len(long_inputs), \
            "Wrong input tokens number"
        
    @pytest.mark.parametrize('model', available_models)
    def test_02_embed_documents(self, model, api_client, project_id):
        embedding = Embeddings(model_id=model,
                               api_client=api_client,
                               project_id=project_id)
        
        generate_embedding = embedding.embed_documents(texts=TestTextEmbeddings.inputs)

        assert isinstance(generate_embedding, list) and \
            isinstance(generate_embedding[0], list) and \
                isinstance(generate_embedding[0][0], float), 'Unexpected return object, should be list[list[float]]'
        
    @pytest.mark.parametrize('model', available_models)
    def test_03_embed_query(self, model, api_client, project_id):
        embedding = Embeddings(model_id=model,
                               api_client=api_client,
                               project_id=project_id)
        
        generate_embedding = embedding.embed_query(text=TestTextEmbeddings.inputs[0])

        assert isinstance(generate_embedding, list) and \
                isinstance(generate_embedding[0], float), 'Unexpected return object, should be list[float]'
        
    @pytest.mark.parametrize('model', available_models)
    def test_04_generate_embeding_params(self, model, api_client, project_id):
        max_input_tokens = 3
        embed_params = {
            EmbedParams.TRUNCATE_INPUT_TOKENS: max_input_tokens,
            EmbedParams.RETURN_OPTIONS: {
            'input_text': True
            }
        }
        embedding = Embeddings(model_id=model,
                               api_client=api_client,
                               project_id=project_id,
                               params=embed_params)
        
        generate_embedding = embedding.generate(inputs=TestTextEmbeddings.inputs)

        assert all([el['input'] == TestTextEmbeddings.inputs[i] for i, el in enumerate(generate_embedding.get('results', []))]), \
            'No field `input` in at least one vector metadata'
        
        assert generate_embedding.get('input_token_count', 0) == len(TestTextEmbeddings.inputs)*max_input_tokens, \
            "Wrong number of tokens"
        
    @pytest.mark.parametrize('model', available_models)
    def test_05_embeddings_serialisation(self, model, project_id):
        from ibm_watsonx_ai.tests.utils import get_wml_credentials
        credentials = get_wml_credentials()
        embedding = Embeddings(model_id=model,
                               credentials=credentials,
                               project_id=project_id)
        
        copied_embedding = Embeddings.from_dict(embedding.to_dict())
        generate_embedding = copied_embedding.generate(inputs=TestTextEmbeddings.inputs)

        assert generate_embedding.get('results'), 'No resulkts section in generated response for copied embedding object'