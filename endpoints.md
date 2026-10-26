# ENTREGABLE (ENDPOINTS QUE CREAMOS NECESARIOS)

## Listado de Endpoints necesarios (Front)

> El front es una app Flask que renderiza templates y consume el backend con `requests` (sin fetch/AJAX desde el navegador). La autenticación es por sesión de Flask. Los formularios HTML solo envían GET y POST: cuando el backend usa PATCH o DELETE, el front recibe un POST y llama al backend con el verbo correcto. Entre paréntesis se indica el endpoint del backend que consume cada ruta.

### 1. Autenticación y Usuarios
* `GET /login` : Formulario de inicio de sesión.
* `POST /login` : Inicia sesión. (`POST /api/auth/login`)
* `GET /registro` : Formulario de registro de cliente.
* `POST /registro` : Crea la cuenta de cliente. (`POST /api/auth/registro`)
* `POST /logout` : Cierra la sesión. (`POST /api/auth/logout`)
* `GET /perfil` : Datos de la sesión: identidad, rol y sucursal si aplica. (`GET /api/auth/me`)

### 2. Cartelera y Sucursales
* `GET /` : Cartelera con filtros de texto, género y clasificación, y paginación. (`GET /api/peliculas`)
* `GET /peliculas/<id>` : Detalle de la película y sus funciones, filtrables por sucursal y fecha. (`GET /api/peliculas/<id>`, `GET /api/peliculas/<id>/funciones`)
* `GET /funciones` : Cartelera de funciones filtrable por sucursal, fecha y película. (`GET /api/funciones`)
* `GET /funciones/<id>` : Detalle de una función: sala, capacidad, precio y disponibilidad. (`GET /api/funciones/<id>`)
* `GET /sucursales` : Sucursales activas. (`GET /api/sucursales`)

### 3. Butacas y Compra de Entradas
* `GET /funciones/<id>/butacas` : Mapa de butacas con su estado (disponible, bloqueada, ocupada, inhabilitada). (`GET /api/funciones/<id>/asientos`)
* `POST /funciones/<id>/butacas` : Inicia la compra con 1 a 6 butacas y las bloquea por 5 minutos. (`POST /api/compras/iniciar`)
* `GET /compras/<id>` : Compra pendiente con temporizador, productos y servicios elegidos. (`GET /api/compras/<id>`, `GET /api/productos`, `GET /api/servicios`, `GET /api/funciones/<id>/cupos-servicios`)
* `POST /compras/<id>/carrito` : Actualiza productos y servicios de la compra pendiente, sin reiniciar el temporizador. (`PATCH /api/compras/<id>`)
* `POST /compras/<id>/abandonar` : Abandona la compra pendiente y libera las butacas. (`DELETE /api/compras/<id>`)
* `POST /compras/<id>/confirmar` : Confirma el pago simulado y genera el QR. (`POST /api/compras/<id>/confirmar`)

### 4. Órdenes y Cancelaciones
* `GET /ordenes/<id>` : Detalle de la orden con importes y QR. (`GET /api/ordenes/<id>`)
* `POST /ordenes/<id>/reenviar-comprobante` : Reenvía el comprobante por mail. (`POST /api/ordenes/<id>/reenviar-comprobante`)
* `POST /ordenes/<id>/cancelar` : Cancela la orden (más de 60 minutos antes de la función) con su reintegro simulado. (`POST /api/ordenes/<id>/cancelar`)

### 5. Candy Bar Independiente
* `GET /candybar` : Catálogo de la sucursal elegida. (`GET /api/candybar/productos`)
* `POST /candybar/pedidos` : Crea el pedido pendiente de pago (máximo 12 unidades por producto). (`POST /api/candybar/pedidos`)
* `GET /candybar/pedidos` : Historial de pedidos del cliente. (`GET /api/candybar/pedidos`)
* `GET /candybar/pedidos/<id>` : Detalle del pedido y QR de retiro. (`GET /api/candybar/pedidos/<id>`)
* `POST /candybar/pedidos/<id>/confirmar` : Confirma el pago simulado y emite el QR de retiro. (`POST /api/candybar/pedidos/<id>/confirmar`)
* `POST /candybar/pedidos/<id>/cancelar` : Cancela un pedido pendiente de pago. (`DELETE /api/candybar/pedidos/<id>`)

### 6. Panel de Empleado (control de acceso e inventario)
* `GET /acceso` : Pantalla de control de acceso de la sucursal.
* `POST /acceso/validar-qr` : Valida el QR de entrada y lo marca como utilizado. (`POST /api/control-acceso/validar-qr`)
* `POST /acceso/entregar-productos` : Entrega los productos de una orden de cine. (`POST /api/control-acceso/entregar-productos`)
* `POST /acceso/validar-servicio` : Valida el uso de un servicio. (`POST /api/control-acceso/validar-servicio`)
* `GET /retiros` : Pantalla de retiros del Candy Bar.
* `POST /retiros/validar` : Consulta un QR de retiro sin consumirlo. (`POST /api/candybar/retiros/validar`)
* `POST /retiros/confirmar` : Confirma la entrega completa del pedido. (`POST /api/candybar/retiros/confirmar`)
* `GET /inventario` : Stock exacto de la sucursal. (`GET /api/sucursales/<id>/inventario`)
* `POST /inventario/ajustar` : Ajusta el inventario. (`POST /api/inventario/ajustar`)
* `POST /candybar/pedidos/<id>/resolver-inventario` : Reingresa o descarta lo no retirado. (`POST /api/candybar/pedidos/<id>/resolver-inventario`)

### 7. Backoffice (Admin)
* `GET /admin` : Panel principal.
* `GET /admin/peliculas/importar` : Buscador de películas en la API externa. (`POST /api/peliculas/buscar-externa`)
* `POST /admin/peliculas/importar` : Importa una película al catálogo local. (`POST /api/peliculas`)
* `GET /admin/funciones/nueva` : Formulario para programar una función. (`GET /api/sucursales`, `GET /api/sucursales/<id>/salas`)
* `POST /admin/funciones` : Crea la función, validando que no se solape. (`POST /api/funciones`)
* `GET /admin/funciones/<id>/cupos` : Cupos de servicios de una función. (`GET /api/funciones/<id>/cupos-servicios`)
* `POST /admin/funciones/<id>/cupos` : Configura los cupos de servicios. (`POST /api/funciones/<id>/cupos-servicios`)
* `GET /admin/servicios` : Catálogo de servicios. (`GET /api/servicios`)
* `POST /admin/servicios` : Alta de servicio. (`POST /api/servicios`)
* `POST /admin/servicios/<id>/editar` : Edita precio, estado o configuración. (`PATCH /api/servicios/<id>`)
* `POST /admin/productos` : Alta de producto. (`POST /api/productos`)
* `GET /admin/candybar/pedidos` : Pedidos del Candy Bar, con filtros y paginación. (`GET /api/candybar/admin/pedidos`)
* `POST /admin/incidencias/reasignar-asiento` : Reasigna una butaca ante una incidencia. (`POST /api/incidencias/reasignar-asiento`)

### 8. Reportes (Admin)
* `GET /admin/reportes/ocupacion` : Ocupación comercial y asistencia por QR. (`GET /api/reportes/ocupacion`)
* `GET /admin/reportes/recaudacion` : Ventas brutas, reintegros y recaudación neta. (`GET /api/reportes/recaudacion`)
* `GET /admin/reportes/cancelaciones` : Cancelaciones con importes y, a pedido, sus motivos. (`GET /api/reportes/cancelaciones`)
