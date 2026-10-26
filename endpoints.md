# ENTREGABLE (ENDPOINTS QUE CREAMOS NECESARIOS)

## Listado de Endpoints necesarios (Front)

### 1. Películas y Cartelera
* `GET /peliculas` : Cartelera de películas.
* `GET /peliculas/<id>` : Detalle de la película y sus funciones disponibles.
* `GET /sucursales` : Locales y salas disponibles.

### 2. Usuarios
* `GET /login` : Formulario de inicio de sesion.
* `POST /login`: Inicia sesion.
* `GET /registro` : Formulario de registro de cliente.
* `POST /registro` : Crea la cuenta del cliente.
* `GET /logout` : Cierra la sesion.
* `GET /perfil` : Perfil del cliente con sus consumos y peliculas vistas.
* `POST /perfil` : Edita los datos del perfil.

### 3. Compra de Entradas
* `GET /funciones/<id>/butacas` : Mapa de butacas de la función (libres y ocupadas).
* `POST /funciones/<id>/butacas` : Bloquea las butacas elegidas y crea la orden.
* `GET /checkout/<id_orden>` : Resumen de la compra y servicios extra.
* `POST /checkout/<id_orden>` : Confirma el pago, genera el QR y envía la factura por mail.

### 4. Compras del cliente
* `GET /compras-cliente` : Historial de compras del cliente.
* `GET /compras-cliente/<id>` : Detalle de una compra con su QR.
* `POST /compras-cliente/<id>/cancelar` : Cancela la compra (hasta 60 min antes de la función).

### 5. Candy Bar
* `GET /candybar` : Catálogo de productos de la sucursal.
* `POST /candybar/pedido` : Realiza el pedido.

### 6. Reseñas (deseable)
* `POST /peliculas/<id>/resena` : Reseña de una película vista (solo si el QR fue validado).

### 7. Backoffice (Admin)
* `GET /admin` : Dashboard principal.
* `GET /admin/estadisticas` : Ocupación, ventas por género, franjas horarias y cancelaciones.
* `GET /admin/peliculas` : Listado de películas cargadas.
* `GET /admin/peliculas/nueva` : Buscador de películas en el catálogo externo.
* `POST /admin/peliculas/nueva` : Carga una película.
* `POST /admin/peliculas/<id>/editar` : Modifica una película.
* `POST /admin/peliculas/<id>/baja` : Da de baja una película.
* `GET /admin/funciones` : Listado de funciones.
* `POST /admin/funciones` : Asigna película a sala, fecha y horario.
* `GET /admin/salas` : Listado de salas.
* `POST /admin/salas` : Configura capacidad y local de una sala.
* `GET /admin/servicios` : Listado de servicios.
* `POST /admin/servicios` : Alta, modificación y baja de servicios.
* `GET /admin/productos` : Listado de productos del Candy Bar.
* `POST /admin/productos` : Alta, modificación y baja de productos.
* `GET /admin/usuarios` : Listado de usuarios.
* `POST /admin/usuarios` : Cambia rol o estado de un usuario.

### 8. Control de Acceso (Empleado)
* `GET /acceso/validar` : Pantalla para validar QR en el ingreso a la sala.
* `POST /acceso/validar` : Valida el QR y lo marca como utilizado.
* `POST /acceso/candybar/<id>/entregar` : Marca como entregado un pedido del Candy Bar.
