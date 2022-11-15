from fastapi import APIRouter, Response
import ormar

from models.item import Item
from models.requests.itemUpdate import ItemUpdate

router = APIRouter()


@router.post('/')
async def add_item(item: Item):
    await item.save()
    return item

@router.get('/')
async def list_item():
    return await Item.objects.all()

@router.get('/{item_id}')
async def get_item(item_id: int):
    try:
        item = await Item.objects.get(id = item_id)
        return item
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "entidade não encontrada"}
        
@router.patch("/{item_id}")
async def patch_papel(propriedade_atualizacao: ItemUpdate, item_id: int, response: Response):
    try:
        item_salvo = await Item.objects.get(id=item_id)
        propriedades_atualizadas = propriedade_atualizacao.dict(exclude_unset=True)
        await item_salvo.update(**propriedades_atualizadas)
        return item_salvo
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "entidade não encontrada"}


@router.delete("/{item_id}")
async def delete_item(item_id: int, response: Response):
    try:
        item = await Item.objects.get(id=item_id)
        return await item.delete()
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada"}
