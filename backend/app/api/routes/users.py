from fastapi import APIRouter

router = APIRouter()


@router.get('/mean')
async def root():
    return "brown"

@router.get('/', name="Ozioma")
async def root():
    return "brown"



@router.get('/mean/login')
async def root():
    return "Ekeledo"


@router.get('/mean/{name}')
async def root(name):
    return name


@router.get('/login')
async def root():
    return "login successful"





