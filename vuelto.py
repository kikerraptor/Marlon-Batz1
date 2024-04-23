def calcular_cambio():
    try:
        monto_compra = float(entry_compra.get())
        monto_pagado = float(entry_pago.get())

        if monto_pagado < monto_compra:
            resultado.set("El pago es insuficiente.")
        else:
            cambio = monto_pagado - monto_compra
            resultado.set(f"El cambio a devolver es: ${cambio:.2f}")
    except ValueError:
        resultado.set("Por favor, ingresa números válidos.")

# Crear ventana principal
ventana = tk()
ventana.title("Calculadora de Vuelto")

# Etiquetas y cajas de texto
tk.Label(ventana, text="Monto de Compra: $").grid(row=0, column=0, padx=10, pady=5)
entry_compra = tk.Entry(ventana)
entry_compra.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Monto Pagado: $").grid(row=1, column=0, padx=10, pady=5)
entry_pago = tk.Entry(ventana)
entry_pago.grid(row=1, column=1, padx=10, pady=5)

# Botón para calcular el cambio
btn_calcular = tk.Button(ventana, text="Calcular Cambio", command=calcular_cambio)
btn_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Resultado
resultado = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado)
resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Ejecutar la ventana
ventana.mainloop()