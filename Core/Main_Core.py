import time
import tkinter as tk

import keyboard
import pyautogui
import win32api
import win32con
from termcolor import *


# =====================================================================================================================
#                                           Funções Auxiliares do programa.
# =====================================================================================================================

# Função para simular um clique do mouse nas coordenadas (x, y).
def click(x, y):
    """Simula um clique do mouse nas coordenadas (x, y)."""
    win32api.SetCursorPos((x, y))
    wait(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Função para simular um clique e liberar imediatamente o botão do mouse.
def click_unpress():
    """Simula um clique e libera o botão do mouse imediatamente."""
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Função para pressionar uma tecla específica no teclado.
def press_key(tecla):
    """Pressiona uma tecla específica no teclado."""
    win32api.keybd_event(tecla, 0, 0, 0)


# Função para liberar uma tecla específica no teclado.
def release_key(tecla):
    """Libera uma tecla específica no teclado."""
    win32api.keybd_event(tecla, 0, win32con.KEYEVENTF_KEYUP, 0)


# Função para aguardar um tempo específico em segundos.
def wait(w):
    """Aguarda um tempo específico em segundos."""
    time.sleep(w)


# Função que faz a automação de pressionar e liberar teclas consecutivamente.
def keys(time, key1, key2, key3, key4):
    """Automatiza a sequência de pressionar e liberar teclas."""
    press_key(key1)
    wait(time)
    release_key(key1)

    press_key(key2)
    wait(time)
    release_key(key2)

    press_key(key3)
    wait(time)
    release_key(key3)

    press_key(key4)
    wait(time)
    release_key(key4)


# =====================================================================================================================
#                                           Funções principais do programa.
# =====================================================================================================================

# Função para controle de parar/continuar o autoclick.
def auto_click(t):
    """Inicia o autoclique e permite parar/continuar pressionando 'q'."""
    print("Pressione 'q' para parar/continuar o autoclique.")
    wait(5)
    while True:
        if keyboard.is_pressed('q'):
            break
        wait(t)
        click_unpress()
        print('Autoclique em andamento.')


# Função para controle de parar/continuar o anti afk.
def anti_afk():
    """Inicia o anti afk e permite parar/continuar pressionando 'q'."""
    print("Pressione 'q' para parar/continuar o anti afk.")
    wait(5)
    while True:
        if keyboard.is_pressed('q'):
            break
        press_key(0x57)  # Pressiona a tecla 'W'
        wait(1)
        press_key(0x53)  # Pressiona a tecla 'S'
        wait(1)
        print('Anti afk em andamento.')


# Função para controle de parar/continuar a automação de ovos.
def auto_egg():
    """Inicia a automação de ovos e permite parar/continuar pressionando 'q'."""
    print("Pressione 'q' para parar/continuar a automação de ovos.")
    wait(5)
    key = 0x045  # Tecla 'E'
    while True:
        if keyboard.is_pressed('q'):
            break
        press_key(key)
        click(821, 669)  # Clica em coordenadas específicas (ajustar conforme necessário)
        wait(2)
        print('autoegg running..')


# Função para retornar ao menu principal.
def menu():
    """Retorna ao menu principal do programa."""
    print("Press 'm' to back to the menu.")
    while True:
        if keyboard.is_pressed('m'):
            break


# =====================================================================================================================
#                                           Funções em BETA
# =====================================================================================================================


# Codigo da GUI (BETA)

# Função de botão da interface para iniciar a automação de ovos.
def auto_egg_open():
    """Função de botão da interface para iniciar a automação de ovos."""
    auto_egg()
    print("Auto Egg Open ativado!")


# Função de botão da interface para iniciar o anti afk.
def anti_afk1():
    """Função de botão da interface para iniciar o anti afk."""
    anti_afk()
    print("Anti AFK ativado!")


# Função de botão da interface para iniciar o autoclique.
def auto_click_gui():
    """Função de botão da interface para iniciar o autoclique."""
    print("tempo padrão de 1.5 segundos por click")
    t = 1.5
    auto_click(t)


# Função de botão da interface para iniciar a automação de eventos (ainda não implementada).
def event_farm():
    """Função de botão da interface para iniciar a automação de eventos (ainda não implementada)."""
    print('Event Farm ativado!')
    event_farm()


# Função de botão da interface para mostrar informações sobre o programa.
def about():
    """Função de botão da interface para mostrar informações sobre o programa."""
    cprint("Made By: exnop (discord)", 'light_magenta')
    print('Current version : 1.0')
    print('launch date: ')


# Função de botão da interface para fechar o programa.
def sair():
    """Função de botão da interface para fechar o programa."""
    root = tk.Tk()
    root.destroy()


# Criação da interface gráfica do programa.
def interface():
    """Criação da interface gráfica do programa."""
    root = tk.Tk()
    root.title("RTK BETA_GUI")
    root.geometry("250x125")
    root.configure(background='gray')

    bg_label = tk.Label(root)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    titulo_label = tk.Label(root, text="Comandos:", font=("Helvetica", 16))
    titulo_label.grid(row=0, column=3, pady=5, )

    auto_egg_button = tk.Button(root, text='auto egg', command=auto_egg_open)
    auto_egg_button.grid(row=1, column=0, pady=3)

    anti_afk_button = tk.Button(root, text='anti afk', command=anti_afk1)
    anti_afk_button.grid(row=1, column=3, pady=3)

    auto_click_button = tk.Button(root, text='auto click', command=auto_click_gui)
    auto_click_button.grid(row=1, column=5, pady=5)

    about_button = tk.Button(root, text="about", command=about)
    about_button.grid(row=2, column=0, pady=5)

    exit_button = tk.Button(root, text='exit', command=sair)
    exit_button.grid(row=2, column=5, pady=5)

    root.mainloop()


# codigo do localizador (BETA)

def locator(tar, time):
    x, y = pyautogui.locateOnScreen(tar)
    while True:
        if keyboard.is_pressed('q'):
            break
        wait(time)
        click(x, y)
