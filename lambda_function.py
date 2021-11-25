# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# RequestHandler


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Willkommen zum Voice Adventure. Wie heißt du?"
        reprompt_text = "Ich heiße Alexa. Wie heißt du?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )


class get_nameHandler(AbstractRequestHandler):
    """Handler for get_name_Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("get_name")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        name = slots["name"].value
        
        speak_output = "Es ist schön dich kennenzulernen, {name}. Das Spiel funktioniert folgendermaßen. Ich werde dir eine Geschichte erzählen in der Du eine entscheidende Rolle spielst. Mit deinen Entscheidungen wirst du die Geschichte leiten. Bist du bereit in das Abenteuer einzutauchen?".format(name=name)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class YesIntentHandler(AbstractRequestHandler):
    """Handler for YesIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("YesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Guten Morgen, du und dein bester Freund Erik Schneider sind Studenten an einer Hochschule. Seit Wochen arbeitet ihr fleißig an einem Gruppenprojekt, welches einen großen Teil der Endnote ausmachen wird. Ihr kommuniziert regelmäßig in der Schule... aber aus unerklärlichen Gründen ist er heute nicht aufgetaucht. Daher entscheidest du dich ihn zu kontaktieren. Willst du Erik auf Whatsapp anschreiben? Erik anrufen? an Erik eine SMS schreiben? Oder zu Eriks Haus gehen?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class NoIntentHandler(AbstractRequestHandler):
    """Handler for NoIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        speak_output = "Kein Problem! Dann bis zum Nächsten mal!"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )        

class WhatsappNachrichtHandler(AbstractRequestHandler):
    """Handler for WhatsappNachricht Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhatsappNachricht")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Du verschickst noch eine Whatsapp Nachricht. Auch hier bleibt nur ein einsames graues Häkchen stehen. Willst du etwas anderes versuchen?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class AnrufenHandler(AbstractRequestHandler):
    """Handler for Anrufen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Anrufen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Du findest Erik in deinen Kontakten und drückst die Anruf-Taste. Nach einer kurzer Pause kommt die Telefonansage. Ihr gewünschter Gesprächspartner ist zurzeit leider nicht erreichbar. Willst du etwas anderes versuchen?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class zu_erik_nach_hause_gehenHandler(AbstractRequestHandler):
    """Handler for zu_erik_nach_hause_gehen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("zu_erik_nach_hause_gehen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Während du mit deinem Fahrrad zu Erik nach Hause gefahren bist, hatte Erik einen tapferen Kampf gegen einen Grizzly Bär geliefert und verstarb. Game over. Willst du es erneut versuchen?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class SMSHandler(AbstractRequestHandler):
    """Handler for SMS Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SMS")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Du schreibst eine SMS an Erik. Was ist los, bro? Ich kann dich schon seit Stunden nicht erreichen. Schreib zurück sobald du kannst.  Das Handy vibriert, plötzlich bekommst du eine Nachricht von Erik. Während ihr miteinander schreibt, erfährst du, dass er sich irgendwo im Nirgendwo befindet und er aber froh ist mit dir zu schreiben. Du frägst ihn was das Letzte ist an was er sich erinnern kann. Erik antwortete: im Keller habe ich... AAA da vorne ist ein Grizzly Bär. Was soll ich tun?! Willst du Erik schreiben, dass er wegrennen, kämpfen oder still stehen soll?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class wegrennenHandler(AbstractRequestHandler) :
    """Handler for wegrennen Intent"""
    def can_handle(self,handler_input) :
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("wegrennen")(handler_input)
    
    def handle(self, handler_input) :
        # type: (HandlerInput) -> Response
        speak_output = "Erik läuft mitten durch den Wald. Er sieht einen Fluss. Beim Versuch den Fluss zu durchqueren, rutscht er auf einem glatten Stein aus. Als er sich aufrappeln will, sieht er dem Bären direkt ins Gesicht. Game Over. Willst du es erneut versuchen?"
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class kaempfenHandler(AbstractRequestHandler) :
    """Handler for kaempfen Intent"""
    def can_handle(self,handler_input) :
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("kaempfen")(handler_input)
    
    def handle(self, handler_input) :
        # type: (HandlerInput) -> Response
        speak_output = "Erik findet zu seiner Rechten einen großen Stein. Er nimmt den Stein, holt aus und wirft ihn mit aller Kraft auf den Bären.  Wutentbrannt läuft der Bär auf Erik zu. Willst du es erneut versuchen?"
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class still_stehenHandler(AbstractRequestHandler) :
    """Handler for still_stehen Intent"""
    def can_handle(self,handler_input) :
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("still_stehen")(handler_input)
    
    def handle(self, handler_input) :
        # type: (HandlerInput) -> response
        speak_output = "Der Bär schaut Erik an und schnüffelt ein wenig an Eriks Beinen. Unbeeindruckt zieht der Bär an Erik vorbei und verschwindet im Gebüsch. Erik bedankt sich bei dir für den Tipp. Nun stellt sich die Frage was er machen soll. Willst du Erik schreiben, dass er tiefer in den Wald, oder versuchen soll, aus dem Wald rauszukommen."
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class aus_dem_waldHandler(AbstractRequestHandler) :
    """Handler for aus_dem_wald Intent"""
    def can_handle(self,handler_input) :
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("aus_dem_wald")(handler_input)
    
    def handle(self, handler_input) :
        # type: (HandlerInput) -> response
        speak_output = "Erik muss dir beichten, dass er einen schlechten Orientierungssinn hat. Er läuft über Fluss und Wälder während er mit dir schreibt. Als du ihn frägst was er eigentlich vorhin sagen wollte, erinnert er sich, dass er  im Keller eine antike Taschenuhr gefunden hat, die er öffnete. Das nächste, woran er sich erinnert ist, dass er plötzlich im Wald war. Daraufhin rätst du ihm, die Uhr genauer anzuschauen und zu öffnen. Ein paar Minuten später ruft dich dein bester Freund an und teilt dir mit, dass er wieder zu Hause im Keller ist.  Happy End"
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class camp_bauenHandler(AbstractRequestHandler) :
    """Handler for camp_bauen Intent"""
    def can_handle(self,handler_input) :
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("camp_bauen")(handler_input)
    
    def handle(self, handler_input) :
        # type: (HandlerInput) -> response
        speak_output = "Als Erik einen ruhigen Platz gefunden hat, wo er Stöcke und Steine zu einem kleinen Zelt aufbauen wollte, wird er mit einem Giftpfeil getroffen und schläft ein. Als er wieder aufwacht, ist er in einem Holzkäfig. Erik schaut sich um und sieht Waldbewohner, die sich im Kreis um ein Lagerfeuer scharen. Erik sieht einen spitzen Stein neben sich liegen. Willst du Erik schreiben, dass er die Ranken an der Tür aufschneiden und fliehen soll, oder lieber erstmal abwarten soll?"
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

class abwartenHandler(AbstractRequestHandler):
    """Handler for abwarten Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("abwarten")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Nach kurzer Zeit versammeln sich die Waldbewohner vor dem Käfig, binden ihn an einem Pfahl und bringen ihn zum Feuer. Willst du es erneut versuchen?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class aufschneiden_und_fliehenHandler(AbstractRequestHandler):
    """Handler for aufschneiden_und_fliehen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("aufschneiden_und_fliehen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Erik rennt schnell ins Gebüsch. Nach einer Weile muss er dir beichten, dass er einen schlechten Orientierungssinn hat. Er läuft über Fluss und Wälder während er mit dir schreibt. Als du ihn frägst, was er eigentlich vorhin sagen wollte, erinnert er sich, dass er  im Keller eine antike Taschenuhr gefunden hat, die er öffnete. Das nächste, woran er sich erinnert ist, dass er plötzlich im Wald war. Daraufhin rätst du ihm, die Uhr genauer anzuschauen und zu öffnen. Ein paar Minuten später ruft dich dein bester Freund an und teilt dir mit, dass er wieder zu Hause im Keller ist. Happy End"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(get_nameHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(WhatsappNachrichtHandler())
sb.add_request_handler(AnrufenHandler())
sb.add_request_handler(zu_erik_nach_hause_gehenHandler())
sb.add_request_handler(SMSHandler())
sb.add_request_handler(wegrennenHandler())
sb.add_request_handler(kaempfenHandler())
sb.add_request_handler(still_stehenHandler())
sb.add_request_handler(aus_dem_waldHandler())
sb.add_request_handler(camp_bauenHandler())
sb.add_request_handler(abwartenHandler())
sb.add_request_handler(aufschneiden_und_fliehenHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()


