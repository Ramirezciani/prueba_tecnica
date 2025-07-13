from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

# Configuración del contexto de encriptación para contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Clave secreta y algoritmo para la generación de tokens JWT
SECRET_KEY = "secret123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Verifica si una contraseña en texto plano coincide con su hash
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# Genera el hash de una contraseña en texto plano
def hash_password(password):
    return pwd_context.hash(password)

# Crea un token de acceso (JWT) con datos y un tiempo de expiración opcional
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()  # Copia los datos a codificar
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))  # Calcula la expiración
    to_encode.update({"exp": expire})  # Agrega la fecha de expiración al token
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Genera y retorna el token JWT
