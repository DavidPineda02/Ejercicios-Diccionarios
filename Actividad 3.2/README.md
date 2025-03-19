# 📚 Proyecto de Investigación

## 📝 Actividades de Contextualización e Identificación de Conocimientos Necesarios para el Aprendizaje

### 🔍 1. Identificación de la función que devuelve el número de elementos en un diccionario

📌 En la mayoría de los lenguajes de programación modernos, existe una función incorporada llamada `len()` (abreviatura de "length" o longitud) que se utiliza para determinar el número de elementos en una colección de datos, incluyendo los diccionarios.

📌 **¿Cómo funciona con diccionarios?**
Cuando aplicas la función `len()` a un diccionario, esta función devuelve la cantidad de pares clave-valor que contiene el diccionario. Cada par clave-valor se cuenta como un elemento único.

---

### ⚖️ 2. Comparación del número de elementos entre dos diccionarios

Para comparar el tamaño de dos diccionarios, se utilizan:

✅ **`len()`**: Permite obtener el número de pares clave-valor presentes en un diccionario.
✅ **Operadores de comparación**: Una vez que tengas el número de elementos de cada diccionario (obtenido con `len()`), puedes utilizar los siguientes operadores para compararlos:
   - `==` (igual a)
   - `!=` (no igual a)
   - `>` (mayor que)
   - `<` (menor que)
   - `>=` (mayor o igual que)
   - `<=` (menor o igual que)

---

### 🗑️ 3. Eliminación de un elemento de un diccionario

📌 **Métodos disponibles:**

- **`del` (declaración)**:
  - Se utiliza para eliminar un par clave-valor específico de un diccionario.
  - Debes especificar la clave del elemento que deseas eliminar.
  - Es una forma directa y eficiente de eliminar elementos individuales.

- **`pop()` (método)**:
  - Elimina un elemento específico del diccionario y devuelve el valor asociado a la clave eliminada.
  - Debes especificar la clave del elemento que deseas eliminar.
  - Es útil cuando necesitas obtener el valor del elemento eliminado.

---

### 📏 4. Función para contar elementos en un diccionario

📌 La función `len()` se utiliza para determinar la cantidad de elementos en un diccionario, devolviendo el número total de pares clave-valor.

---

### 🚮 5. Eliminación de todos los elementos de un diccionario

📌 **Método `clear()`**:

✅ **Función**:
- Vacía completamente un diccionario, eliminando todos sus pares clave-valor.

✅ **Cómo funciona**:
- Modifica el diccionario original, dejándolo vacío.
- Después de utilizar `clear()`, el diccionario sigue existiendo pero sin elementos.

✅ **Usos comunes**:
- Reutilizar un diccionario asegurándose de que esté vacío antes de agregar nuevos elementos.
- Liberar memoria ocupada por los elementos del diccionario.

---

### 🔎 6. Uso de `direccion_datos.values()`

📌 **Propósito principal**:
- Se utiliza para obtener una vista de todos los valores almacenados en un diccionario.
- Extrae todos los valores de los pares clave-valor y los presenta en un formato iterable.

📌 **Qué devuelve**:
- No devuelve una lista tradicional, sino una "vista" dinámica que se actualiza si el diccionario cambia.
- Contiene todos los valores asociados a las claves del diccionario.

---

### 🗂️ 7. Uso de `direccion_datos.items()`

📌 **Propósito principal**:
- Se utiliza para obtener una vista de todos los pares clave-valor de un diccionario.
- Extrae tanto las claves como los valores y los presenta en un formato iterable de tuplas.

📌 **Qué devuelve**:
- No devuelve una lista tradicional, sino una "vista" dinámica que se actualiza si el diccionario cambia.
- La vista contiene tuplas, donde cada tupla representa un par clave-valor.

---

### 🔄 8. Agregar elementos de un diccionario a otro

📌 **Método `update()`**:

✅ **Función principal**:
- Fusiona los elementos de un diccionario en otro.
- Si hay claves duplicadas, los valores del diccionario que se está agregando sobrescriben los valores del diccionario original.

✅ **Cómo funciona**:
- Modifica el diccionario original, agregando o actualizando los pares clave-valor del diccionario pasado como argumento.
- Puede aceptar como argumento otro diccionario o un iterable de pares clave-valor.

📌 **¡Y eso es todo!** Con estos métodos y funciones, puedes manipular y gestionar diccionarios de manera eficiente. 🚀

