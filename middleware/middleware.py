from django.contrib.auth.models import User
from contract.models import Contract  # Import your Contract model
from django.utils.functional import SimpleLazyObject

class ContractMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the user is authenticated, try to get the Contract
        if request.user.is_authenticated:
            contract = Contract.objects.filter(employeeuser__user=request.user, is_active=True).first()
            request.contract = SimpleLazyObject(lambda: contract)
        else:
            request.contract = None

        response = self.get_response(request)

        return response