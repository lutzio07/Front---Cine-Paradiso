# ENTREGABLE (ENDPOINTS QUE CREAMOS NECESARIOS)

## Listado de Endpoints necesarios (Front)

> El front es una app Flask que renderiza templates y consume el backend con `requests` (sin fetch/AJAX desde el navegador). Los formularios HTML solo envían GET y POST: cuando el backend usa PATCH o DELETE, el front recibe un POST y llama al backend con el verbo correcto. Entre paréntesis se indica el endpoint del backend que consume cada ruta. Roles: administrador y cliente.

### 1. Usuarios y sesión
* `GET /login` : Formulario de inicio de sesión.
* `POST /login` : Inicia sesión. (`POST /api/sesiones`)
* `GET /registro` : Formulario de registro de cliente.
* `POST /registro` : Crea la cuenta de cliente. (`POST /api/usuarios`)
* `POST /logout` : Cierra la sesión. (`DELETE /api/sesiones`)
* `GET /perfil` : Datos del usuario, consumos y películas vistas. (`GET /api/usuarios/me`, `GET /api/ordenes`)
* `POST /perfil` : Edita los datos del perfil. (`PATCH /api/usuarios/me`)

### 2. Cartelera y sucursales
* `GET /` : Cartelera con filtros de texto, género y clasificación, y paginación. (`GET /api/peliculas`)
* `GET /peliculas/<id>` : Detalle de la película y sus funciones, filtrables por sucursal y fecha. (`GET /api/peliculas/<id>`, `GET /api/peliculas/<id>/funciones`)
* `GET /funciones` : Funciones filtrables por sucursal, fecha y película. (`GET /api/funciones`)
* `GET /sucursales` : Sucursales y capacidad de sus salas. (`GET /api/sucursales`, `GET /api/sucursales/<id>/salas`)

### 3. Compra de entradas y servicios
* `GET /funciones/<id>/butacas` : Mapa de butacas libres y ocupadas. (`GET /api/funciones/<id>/asientos`)
* `POST /funciones/<id>/butacas` : Crea la orden y bloquea las butacas elegidas. (`POST /api/ordenes`)
* `GET /checkout/<id_orden>` : Resumen de la compra y servicios disponibles. (`GET /api/ordenes/<id>`, `GET /api/servicios`)
* `POST /checkout/<id_orden>/servicios` : Agrega o quita servicios de la orden. (`PATCH /api/ordenes/<id>`)
* `POST /checkout/<id_orden>/pago` : Confirma el pago, genera el QR y envía la factura por mail. (`POST /api/ordenes/<id>/pagos`)
* `POST /checkout/<id_orden>/abandono` : Abandona la orden pendiente y libera las butacas. (`DELETE /api/ordenes/<id>`)

### 4. Mis compras
* `GET /mis-compras` : Historial de compras del cliente. (`GET /api/ordenes`)
* `GET /mis-compras/<id>` : Detalle de una compra con su QR. (`GET /api/ordenes/<id>`)
* `POST /mis-compras/<id>/cancelacion` : Cancela la compra hasta el plazo permitido. (`POST /api/ordenes/<id>/cancelaciones`)

### 5. Reseñas (deseable)
* `POST /peliculas/<id>/resenas` : Reseña de una película vista, solo si el QR fue validado. (`POST /api/peliculas/<id>/resenas`)

### 6. Backoffice (Admin)
* `GET /admin` : Panel principal con los dashboards.
* `GET /admin/estadisticas` : Ocupación, ventas por género, franjas horarias y cancelaciones. (`GET /api/reportes/ocupacion`, `/ventas-por-genero`, `/franjas-horarias`, `/cancelaciones`)
* `GET /admin/peliculas/importar` : Busca películas en la API externa. (`GET /api/catalogo/peliculas?buscar=`)
* `POST /admin/peliculas` : Carga una película al catálogo. (`POST /api/peliculas`)
* `POST /admin/peliculas/<id>/edicion` : Modifica una película. (`PATCH /api/peliculas/<id>`)
* `POST /admin/peliculas/<id>/baja` : Da de baja una película. (`DELETE /api/peliculas/<id>`)
* `GET /admin/funciones` : Listado de funciones y salas con su capacidad. (`GET /api/funciones`)
* `POST /admin/funciones` : Asigna película a sala, local, fecha y horario. (`POST /api/funciones`)
* `POST /admin/funciones/<id>/edicion` : Modifica una función. (`PATCH /api/funciones/<id>`)
* `POST /admin/funciones/<id>/baja` : Cancela una función. (`DELETE /api/funciones/<id>`)
* `GET /admin/servicios` : Listado de servicios. (`GET /api/servicios`)
* `POST /admin/servicios` : Alta de servicio. (`POST /api/servicios`)
* `POST /admin/servicios/<id>/edicion` : Modifica un servicio. (`PATCH /api/servicios/<id>`)
* `POST /admin/servicios/<id>/baja` : Da de baja un servicio. (`DELETE /api/servicios/<id>`)
* `GET /admin/ingreso` : Pantalla de validación del QR en el ingreso a la sala.
* `POST /admin/ingreso` : Valida el QR y lo marca como utilizado. (`PATCH /api/codigos-qr/<codigo>`)
* `GET /admin/reportes/ventas.pdf` (deseable) : PDF de ventas por función y películas más vistas. (`GET /api/reportes/ventas?formato=pdf`)
