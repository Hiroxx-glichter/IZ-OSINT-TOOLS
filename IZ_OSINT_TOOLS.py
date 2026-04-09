import os, time, subprocess

# --- Configuración Estética de Colores (Parrot Style) ---
W, G, VG, R, C, B, RESET = '\033[97m', '\033[92m', '\033[1;92m', '\033[91m', '\033[96m', '\033[1m', '\033[0m'
LINE = f"{W}{B}======================================================================{RESET}"

# --- Info Dinámica del Sistema ---
try:
    USER, HOST = subprocess.getoutput("whoami"), subprocess.getoutput("hostname")
except:
    USER, HOST = "live", "parrot"

def clear():
    # Detecta el sistema para usar cls en Windows o clear en Linux
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    # --- LA LUPA LEGENDARIA (Con mango largo y elegante) ---
    # Alineada línea por línea con el cuadro de créditos
    print(f"{W}{B}                 弄弄弄弄弄弄弄弄弄弄弄{RESET}")
    print(f"{W}{B}             弄弄                      弄弄     {G} ___________________________{RESET}")
    print(f"{W}{B}           弄弄                          弄弄    {G}|                           |{RESET}")
    print(f"{W}{B}          弄弄        {R}____________        {W}弄弄   {G}|    {C}IZ OSINT TOOLS v2.5{G}    |{RESET}")
    print(f"{W}{B}         弄弄        {R}|            |       {W}弄弄   {G}|                           |{RESET}")
    print(f"{W}{B}         弄弄        {R}|      ?     |       {W}弄弄   {G}|    {VG}CODE BY: IZ4CXZ_BY{G}     |{RESET}")
    print(f"{W}{B}         弄弄        {R}|____________|       {W}弄弄   {G}|___________________________|{RESET}")
    print(f"{W}{B}          弄弄                          弄弄{RESET}")
    print(f"{W}{B}           弄弄                        弄弄{RESET}")
    print(f"{W}{B}             弄弄                    弄弄{RESET}")
    print(f"{W}{B}                 弄弄弄弄弄弄弄弄弄弄弄{RESET}")
    print(f"{W}{B}                       弄弄{RESET}")
    print(f"{W}{B}                         弄弄{RESET}")
    print(f"{W}{B}                           弄弄{RESET}")
    print(f"{W}{B}                             弄弄{RESET}")
    print(f"{W}{B}                               弄弄{RESET}")
    print(f"{W}{B}                                 弄弄{RESET}")
    print(f"{W}{B}                                   弄弄{RESET}")
    print(f"{W}{B}                                     弄弄{RESET}")
    print(f"{W}{B}                                       弄弄{RESET}")
    print(f"{W}{B}                                         弄弄{RESET}")
    
    # --- Nombre de la herramienta ---
    print(f"{C}{B}                I Z   O S I N T   T O O L S{RESET}")
    
    # --- SECCIÓN DE CONTACTO (Arriba, debajo del nombre) ---
    print(f"{LINE}")
    print(f"{W}[ {VG}CONTACT {W}]")
    print(f"{G}By: Iz4cxz_by")
    print(f"{G}https://github.com/Hiroxx-glichter")
    print(f"{LINE}")

def menu():
    clear()
    print_header()
    # --- MENÚ DE HERRAMIENTAS (Con flujo CD && ejecución corregido) ---
    print(f"\n{W}{B} [ SELECT A TOOL ]{RESET}")
    print(f"{LINE}")
    # Herramientas y descripciones breves
    tools = [
        ("PhoneSploit", "ADB Android Exploit"), 
        ("FinalRecon", "All-in-One Recon"), 
        ("SocialScan", "Email/User Check"), 
        ("SQLMap", "Database Exploit"), 
        ("Mr. Holmes", "Info Gathering"), 
        ("GhostTrack", "Location Tracker"), 
        ("MedusaPhiser", "Phishing Tool"), 
        ("Exit", "")
    ]
    # Genera el menú numérico automáticamente
    for i, (name, desc) in enumerate(tools, 1):
        color = R if name == "Exit" else G
        print(f"{VG}  {i}.{RESET} {color} {name.ljust(15)} {W}>>  ({desc}){RESET}")
    print(f"{LINE}")

def main():
    # Ruta centralizada para todas las herramientas en ~/OSINT/
    path = os.path.expanduser("~/OSINT/")
    
    while True:
        menu()
        opt = input(f"\n{VG}{USER}@{HOST}{W}:{G}~$ {RESET}")
        
        # --- LÓGICA DE NAVEGACIÓN (Corregida) ---
        if opt == "1":
            # PhoneSploit-Pro dentro de ~/OSINT/
            os.system(f"cd {path}PhoneSploit-Pro && python3 phonesploitpro.py")
        elif opt == "2":
            u = input(f"\n{W}URL: {RESET}")
            # FinalRecon dentro de ~/OSINT/
            os.system(f"cd {path}OSINT_FinalRecon && python3 finalrecon.py --full {u}")
        elif opt == "3":
            t = input(f"\n{W}Target (Email/User): {RESET}")
            # SocialScan se asume instalado en el PATH
            os.system(f"socialscan {t}")
        elif opt == "4":
            u = input(f"\n{W}URL: {RESET}")
            # SQLMap se asume instalado en el PATH o en ~/OSINT/
            os.system(f"sqlmap -u '{u}' --dbs --batch")
        elif opt == "5": 
            # Mr. Holmes dentro de ~/OSINT/ con punto
            # SOLUCIÓN DEFINITIVA PARA Mr. Holmes:
            # sudo -E lleva las librerías de tu usuario normal (pyqrcode) al entorno de root
            os.system(f"cd {path}Mr.Holmes && sudo -E python3 MrHolmes.py")
        elif opt == "6": 
            # GhostTrack dentro de ~/OSINT/
            os.system(f"cd {path}GhostTrack && python3 GhostTR.py")
        elif opt == "7": 
            # MedusaPhisher dentro de ~/OSINT/
            # Se usa bash y sudo para asegurar permisos en el script .sh
            os.system(f"cd {path}MedusaPhisher && sudo chmod +x medusa_phisher.sh && sudo bash medusa_phisher.sh")
        elif opt == "8": 
            break
        else:
            print(f"{R}\nInvalid Option! Press Enter to try again.{RESET}")
            time.sleep(1)
            continue
        
        # Pausa para ver los resultados antes de limpiar la pantalla
        input(f"\n{G}Done. Press Enter to return to menu...{RESET}")

if __name__ == "__main__":
    # Asegura que el script corra solo cuando se ejecuta directamente
    main()
