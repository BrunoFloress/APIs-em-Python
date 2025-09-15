import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

ultima_img = None  # garante que a variável existe no escopo global

def gerar_qr_code():
    texto = entrada.get()
    if not texto.strip():
        messagebox.showwarning("Aviso", "Por favor, insira um texto ou link válido para gerar o QR Code.")
        return

    # Gerando o QR Code corretamente
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    # Cria imagem PIL e converte para RGB (necessário para ImageTk)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Redimensiona para exibir (use NEAREST para manter os pixels nítidos)
    img_resized = img.resize((200, 200), Image.NEAREST)
    img_tk = ImageTk.PhotoImage(img_resized)

    # Atualiza o label com a imagem
    lbl_img.config(image=img_tk)
    lbl_img.image = img_tk

    # Habilita botão de salvar
    btn_salvar.config(state=tk.NORMAL)

    global ultima_img
    ultima_img = img  # guarda a imagem PIL original para salvar

def salvar_qrcode():
    global ultima_img
    if ultima_img is None:
        messagebox.showwarning("Aviso", "Nenhum QR Code gerado para salvar.")
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
    )
    if caminho:
        ultima_img.save(caminho)
        messagebox.showinfo("Sucesso", f"QR Code salvo em:\n{caminho}")

# Configurando a janela principal
root = tk.Tk()
root.title("Gerador de QR Code")
root.geometry("400x400")

# Entrada de texto
tk.Label(root, text="Digite o texto ou o link:").pack(pady=5)
entrada = tk.Entry(root, width=40)
entrada.pack(pady=5)

# Botão Gerar
btn_gerar = tk.Button(root, text="Gerar QR Code", command=gerar_qr_code)
btn_gerar.pack(pady=5)

# Label para exibir a imagem
lbl_img = tk.Label(root)
lbl_img.pack(pady=10)

# Botão Salvar (inicialmente desabilitado)
btn_salvar = tk.Button(root, text="Salvar QR Code", state=tk.DISABLED, command=salvar_qrcode)
btn_salvar.pack(pady=5)

root.mainloop()
