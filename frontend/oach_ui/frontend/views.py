from django.shortcuts import render, redirect
from ldap3 import Server, Connection, ALL
from .models import EnvironmentData, LdapConfig, AppUser, Transaction, TransactionParameter
from .serializers import AppUserSerializer
import uuid, json

ldap_host = ''
ldap_port = 0
ldap_base_dn = ''
ldap_search_field = ''
ldap_acc = ''
ldap_pwd = ''

primary_division = ''

def useruid(s, login):
    """Connect to a LDAP and check the uid matching the given field data"""
    uid = False
    c = Connection(s, ldap_acc, password=ldap_pwd, auto_bind=True)

    if c.result['description'] != "success":
        raise Exception(f'LDAP connection using service account {ldap_acc} failed.')

    # Look for the user entry.
    if not c.search(ldap_base_dn, "(" + ldap_search_field + "=" + login + ")") :
        raise Exception(f'Login {login} not found.')
    else:
        if len(c.entries) > 0:
            uid = c.entries[0].entry_dn
        else:
            raise Exception(f'Login {login} not found.')
        c.unbind()
    return uid

def try_ldap_login(login, password):
    """ Connect to a LDAP directory to verify user login/passwords"""
    result = False
    try: 
        s = Server(ldap_host, port=ldap_port, use_ssl=False, get_info=ALL)
        # 1. connection with service account to find the user uid
        uid = useruid(s, login)
    
        if uid: 
            # 2. Try to bind the user to the LDAP
            c = Connection(s, user = uid , password = password, auto_bind = True)
            c.open()
            c.bind()
            result =  c.result['description'] == 'success' # "success" if bind is ok
            c.unbind()
    except Exception as e:
        print(f'Error: {str(e)}')
    return result

def getTransactionParameters(trans_name):
    trans_url_param = 'RequestURL'
    trans_url_value = ''
    trans_auth_param = 'Authorization'
    trans_auth_value = ''
    try:
        backend_transactions = Transaction.objects.filter(TransactionName=trans_name)
        if (len(backend_transactions) == 0):
            raise Exception(f'Transaction - {trans_name} is not found.')
        try:
            trans_url_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_url_param).first().ParameterValue
        except Exception:
            raise Exception(f'Transaction - {trans_name} Request URL is not found.')
        try:
            trans_auth_value = TransactionParameter.objects.filter(TransactionName=backend_transactions.first().id).filter(ParameterName=trans_auth_param).first().ParameterValue
        except Exception:
            raise Exception(f'Transaction - {trans_name} Authorization is not found.')
        if not trans_url_value:
            raise Exception(f'Transaction - {trans_name} Request URL is not found.')
        if not trans_auth_value:
            raise Exception(f'Transaction - {trans_name} Authorization is not found.')
        return {
            'RequestURL': trans_url_value,
            'Authorization': trans_auth_value,
        }
    except Exception as e:
        print(str(e))
        return {
            'RequestURL': '',
            'Authorization': '',
        }

def login(request, *args, **kwargs):
    global ldap_host, ldap_port, ldap_base_dn, ldap_search_field, ldap_acc, ldap_pwd, primary_division
    env_name = EnvironmentData.objects.filter(Name='Environment Name')[0].Value
    primary_division = ''
    if (not ldap_host or not ldap_port or not ldap_base_dn or not ldap_search_field or not ldap_acc or not ldap_pwd):
        ldap_config = LdapConfig.objects.all()[0]
        ldap_host = ldap_config.host
        ldap_port = int(ldap_config.port)
        ldap_base_dn = ldap_config.base_dn
        ldap_search_field = ldap_config.search_field
        ldap_acc = ldap_config.ldap_acc
        ldap_pwd = ldap_config.password
    login_error = 'The user ID or password that you entered is incorrect. Please check the spelling and try again.'
    error_message = ''
    if request.method == 'POST':
        user = request.POST.get('OACHUserName', '').lower()
        password = request.POST.get('OACHPassword', '')
        if (not user and not password):
            error_message = login_error
        if not try_ldap_login(user, password):
            error_message = login_error
        else:
            request.session['oach-session-id'] = f'{user}-{str(uuid.uuid4().hex)}'
            return redirect('oach-home')
    else:
        try:
            oach_session_id = request.session['oach-session-id']
            return redirect('oach-home')
        except KeyError:
            pass
    return render(request, 'frontend/login.html', { 'env_name': env_name, 'error_message': error_message })

def logout(request, *args, **kwargs):
    global primary_division
    try:
        primary_division = ''
        del request.session['oach-session-id']
    except KeyError:
        pass
    return redirect('oach-login')
    
def index(request, *args, **kwargs):
    try:
        global primary_division
        oach_session_id = request.session['oach-session-id']
        login = oach_session_id.split('-')[0]
        user = AppUser.objects.filter(login=login)[0]
        user_full_name = f'{user.first_name} {user.last_name}'
        user_email_addr = user.email_addr
        oach_user_data = AppUserSerializer(user).data
        is_one_primary = user.Department.count() == 1
        if is_one_primary:
            primary_division = user.Department.first().name
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            primary_division = data.get('selected_division')
        search_account_trans_params = getTransactionParameters('Search Account By Account Number')
        account_hier_trans_params = getTransactionParameters('Get Account Hierarchy By Customer Account Id')
        asset_hier_trans_params = getTransactionParameters('Get Asset By Account Id')
        order_hier_trans_params = getTransactionParameters('Get Order By Account Id')
        invoice_trans_params = getTransactionParameters('Get Invoice By Billing Account Id')
        search_asset_pav_trans_params = getTransactionParameters('Search Asset By PAV')
        cti_event_trans_params = getTransactionParameters('Subscribe To CTI Events')
        cti_event_trans_params['RequestURL'] = cti_event_trans_params['RequestURL'].replace('<login>', login)
        session_data = json.dumps({
            'oach_session_id': oach_session_id,
            'oach_user_data': oach_user_data,
            'primary_division': primary_division,
            'is_one_primary': is_one_primary,
            'search_account_trans_params': search_account_trans_params,
            'account_hier_trans_params': account_hier_trans_params,
            'asset_hier_trans_params': asset_hier_trans_params,
            'order_hier_trans_params': order_hier_trans_params,
            'invoice_trans_params': invoice_trans_params,
            'cti_event_trans_params': cti_event_trans_params,
            'search_asset_pav_trans_params': search_asset_pav_trans_params,
        })
        return render(request, 'frontend/index.html', {
            'oach_session_id': oach_session_id ,
            'session_data': session_data,
            'user_full_name': user_full_name,
            'user_email_addr': user_email_addr,
        })
    except KeyError:
        return redirect('oach-login')