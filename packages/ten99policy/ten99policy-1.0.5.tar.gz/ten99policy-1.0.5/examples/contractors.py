import ten99policy
ten99policy.api_key = "t9sk_live_db68a311-e4b4-4ee8-b2d6-238bc97d83ed"

# You can configure the environment for 1099Policy API (sandbox|production)
# ten99policy.environment = 'sandbox'


# -----------------------------------------------------------------------------------*/
# Fetching the list of contractors
#-----------------------------------------------------------------------------------*/

# resource = ten99policy.Contractors.list(
#     email='harold@gmail.com',
# )

resource = ten99policy.Contractors.modify('cn_xW5Bu6UPWu',
    email='john.doe@gmail.com',
    first_name="George"
)


print(resource)
