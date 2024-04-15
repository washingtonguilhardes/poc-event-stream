from flask import Flask, Response,json
import time
import random

app = Flask(__name__)

# Rota para enviar eventos SSE
@app.route('/events')
def events():
    def generate():
        # Define o tipo de conteúdo como text/event-stream
        yield 'Content-Type: text/event-stream\n\n'

        message = """
          Et culpa eiusmod tempor est nostrud proident consectetur Lorem irure. Minim qui adipisicing minim duis veniam amet tempor non non sint est. Voluptate ad minim qui sint Lorem ut sint ad ipsum excepteur consequat sint cillum veniam.Enim et duis sit eiusmod nulla anim esse eu esse labore eiusmod eu. Eu ut esse esse sunt id mollit minim laborum ex veniam aute magna.

          Non occaecat nisi ipsum commodo elit nulla incididunt fugiat. Ea officia quis aliqua Lorem sint eu culpa magna elit cupidatat enim nulla eiusmod exercitation. Laborum magna ex dolor adipisicing ut non. Velit id est laborum eiusmod quis.

          Eu reprehenderit duis id amet pariatur. Cillum fugiat in ea officia elit aute enim laborum et proident sint dolore. Ipsum ut aute labore velit labore cupidatat cillum proident. Ad consectetur nisi irure do laboris anim sint excepteur et eu.

          Incididunt ullamco nulla est consequat consectetur reprehenderit mollit tempor ut consequat mollit. Sint ullamco minim esse velit laborum laboris ipsum qui nisi magna reprehenderit fugiat aute adipisicing. Do voluptate magna Lorem nulla laboris occaecat officia sit do sit incididunt cupidatat Lorem. Lorem ea qui cillum eiusmod ut ullamco cillum mollit. Occaecat sint voluptate laborum anim occaecat ipsum.

          Aliquip cillum minim ea excepteur culpa. Elit laborum commodo culpa ut dolore duis deserunt excepteur elit velit. Aliqua exercitation tempor elit sit elit.

          Labore sunt sunt sunt exercitation consequat enim esse aliqua reprehenderit irure adipisicing. Fugiat consequat commodo minim anim deserunt nostrud dolor eiusmod elit eu dolor ex. Excepteur sit nostrud culpa quis tempor anim ex consectetur magna eu elit duis. Anim sit veniam labore elit dolore sint aute incididunt ex ullamco officia dolor labore. Consectetur proident officia non eu fugiat in duis magna do. Mollit amet elit anim est laboris velit. Adipisicing proident amet labore dolor nostrud non consequat aliquip Lorem minim.

          Do aute sunt nulla quis ex adipisicing sit consectetur ipsum sunt esse ad velit. Cupidatat proident exercitation aliqua et aute labore. Occaecat sunt consectetur pariatur minim et. Reprehenderit labore veniam voluptate incididunt qui.
          """



        # Envia uma mensagem a cada segundo
        pointer = 10
        feedbackTime = [10, 30, 50, 70, 80, 90, 100, 150, 200, 300]
        while pointer < len(message):
            # Gera um evento com dados
            data = { "message": message[0:pointer], "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')}
            pointer += 10
            # Envia o evento
            yield 'data: {}\n\n'.format(json.dumps(data))
            time.sleep(random.choice(feedbackTime) / 1000)

    return Response(generate(), content_type='text/event-stream')

@app.route('/')
def index():
    f = open("../index.html", "r")

    return Response(f.read(), content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True, port = 4000, host='0.0.0.0')