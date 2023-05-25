from amocrm.v2 import tokens, Lead


#tokens.default_token_manager.init(code="def50200b80be6de544195eaeb741fa5ad186ad7f7f46388484ae199f53af7f735c8a622b5899c3df53a9ae8f1a115cfcfdfeb5a2ba742c326bf2428e4944f10ab1b07e1442115910e9b77c1d045aecb7f69c0b84904e9a50b32a01fdc8e8c20591f9d9f4d08d86d13628a8667b5f499cc65c7be929d19dbf3a6a556980f91bd2d581c40d4f0583bdf5be257c89f113c69506063e244e9b282ba07fac0c757feb7b2c7b63894a4e03c694b6e3de036c2360f300e088dafc112a1b9c7b36cfd33f74fc33f979307e7a9efc692a0e988e8235bab9ba924de73a7027b2c77556deae5d9fd356911f841e6bafaa28f09245372959e051031a22024f86526257797d40b434ab83193f034aa7448e8a4d1129ae55cbbeaa9c062d34baaf31426b9f883710afd39ecafa816a912eaed3d28243bf3b2033c226c71cf1d9dc3d4652d21064fdbdade4f017eca7bfb4b777ff2a51274e6afda7198c4295f72d27921743793e7faf203cd7eb1fdaea0b7fafe7fd470749b605d7ad3dc76a1bf648c42c4af57064a93d9834d2e7e5104cbca08d2641f4cc14b011916880cd613630d06e2f64def5a00c7be603e4c6fca8e925b941e4d4b864d97b008c417fbd730b2a7fc5a70fa849bb62b61af8eaa266c2f0cf1abe08b3c1b687885941e48c2142dad")

def get_lead_ids():
    tokens.default_token_manager(
        client_id="da849176-271d-4626-9d25-639d627a072c",
        client_secret="RvxEron4C4Bh8kIKvwWkmjdwkkeJNcUPUgc9jKWoWRqiGHF2FDWjXsdm6CiOtuuN",
        subdomain="turkeyre",
        redirect_url="https://ya.ru",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )
    resp = {}
    for lead in Lead.objects.all():
        resp[lead.id] = False
        for tag in lead.tags:
            if tag.name == '00':
                resp[lead.id] = True
    return resp


def change_tag(lead_id: int):
    tokens.default_token_manager(
        client_id="da849176-271d-4626-9d25-639d627a072c",
        client_secret="RvxEron4C4Bh8kIKvwWkmjdwkkeJNcUPUgc9jKWoWRqiGHF2FDWjXsdm6CiOtuuN",
        subdomain="turkeyre",
        redirect_url="https://ya.ru",
        storage=tokens.FileTokensStorage(),
    )
    lead = Lead.objects.get(lead_id)
    tags_to_add = []
    for tag in lead.tags:
        tags_to_add.append(tag.name)
    if '00' in tags_to_add:
        tags_to_add.remove("00")
        lead.tags = []
        lead.save()
        for i in tags_to_add:
            lead.tags.append(i)
        lead.save()


