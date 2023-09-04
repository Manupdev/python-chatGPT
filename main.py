import openai 
import config 
import typer
from rich import print 
from rich.table import Table

def main():

    openai.api_key = config.api_key

    print("[bold green] ChatGPT API [/bold green]")

    table = Table("Comando", "Descripcion")
    table.add_row("exit", "salir de la aplicacion")
    table.add_row("new", "nueva pregunta")

    print(table)

    context = {"role":"system", "content": "Eres un asistente muy útil."}

    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("Nueva Pregunta: ")
            messages = [context]
            content = __prompt()
        messages.append({"role":"user", "content": content})

        response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages= messages)

        response_content = response.choices[0].message.content

        messages.append({"role":"assistant", "content": response_content})

        print(f"[bold green]>[/bold green][green]{response_content}[/green]")



def __prompt() -> str :
    prompt = typer.prompt("\nQue quieres preguntar ? ")

    if prompt == "exit":
        exit = typer.confirm("Estas seguro??")
        if exit:
            print("Hasta Luego!")
            raise typer.Abort()
        return __prompt()
    return prompt


if __name__ == "__main__":
    typer.run(main)



