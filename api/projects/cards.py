from core.rest_client import RestClient

class Cards(RestClient):

    def list_project_cards(self, column_id, **kwargs):
        """
        https://developer.github.com/v3/projects/cards/#list-project-cards
        """
        hearders = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.get('/projects/columns/{}/cards'.format(column_id), hearders = hearders, **kwargs)

    def get_a_project_card(self, card_id):
        """
        https://developer.github.com/v3/projects/cards/#get-a-project-card
        """
        hearders = {'Accept': 'application/vnd.github.inertia-preview+json'}
        return self.get('/projects/columns/cards/{}'.format(card_id), hearders = hearders)

    def create_a_project_card(self, column_id, **kwargs):
        """
        https://developer.github.com/v3/projects/cards/#create-a-project-card
        """
        hearders = {'Accept': 'application/vnd.github.inertia-preview+json'}
        return self.post('/projects/columns/{}/cards'.format(column_id), hearders = hearders, **kwargs)

    def update_a_project_card(self, card_id, **kwargs):
        """
        https://developer.github.com/v3/projects/cards/#update-a-project-card
        """
        hearders = {'Accept': 'application/vnd.github.inertia-preview+json'}
        return self.patch('/projects/columns/cards/{}'.format(card_id), hearders = hearders, **kwargs)

    def delete_a_project_card(self, card_id):
        """
        https://developer.github.com/v3/projects/cards/#delete-a-project-card
        """
        hearders = {'Accept': 'application/vnd.github.inertia-preview+json'}
        return self.delete('/projects/columns/cards/{}'.format(card_id), hearders = hearders)

    def move_a_project_card(self, card_id, **kwargs):
        """
        https://developer.github.com/v3/projects/cards/#move-a-project-card
        """
        hearders = {'Accept': 'application/vnd.github.inertia-preview+json'}
        return self.post('/projects/columns/cards/{}/moves'.format(card_id),hearders = hearders, **kwargs)
