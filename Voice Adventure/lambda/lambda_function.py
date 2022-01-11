# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

# initialize persistence adapter
import os
import boto3
from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_dynamodb.adapter import DynamoDbAdapter

# initialize persistence adapter
ddb_region = os.environ.get('DYNAMODB_PERSISTENCE_REGION')
ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')

ddb_resource = boto3.resource('dynamodb', region_name=ddb_region)
dynamodb_adapter = DynamoDbAdapter(table_name=ddb_table_name, create_table=False, dynamodb_resource=ddb_resource)

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



def handle(self, handler_input):
    # type: (HandlerInput) -> Response
    attr = handler_input.attributes_manager.persistent_attributes
    if not attr:
        attr['counter'] = 0
        attr['state'] = 'ENDED'

    handler_input.attributes_manager.session_attributes = attr

    handler_input.attributes_manager.save_persistent_attributes()
    speak_output = ("Welcome back. Your saved counter is {}. You can say Hello or Help?".format(attr["counter"]))
    reprompt = "Say hello or help to start."
    return (
        handler_input.response_builder
            .speak(speak_output)
            .ask(reprompt)
            .response
    )

def handle(self, handler_input):
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr['state'] = "STARTED"
    session_attr["counter"] += 1
    handler_input.attributes_manager.persistent_attributes = session_attr
    handler_input.attributes_manager.save_persistent_attributes()

    speak_output = ("Hi there, Hello World! Your saved counter is {}.".format(session_attr["counter"]))
    return (
        handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
    )    

# RequestHandler


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        # extract persistent attributes, if they exist
        attr = handler_input.attributes_manager.persistent_attributes
        attributes_exist = ('name' in attr)
        if attributes_exist:
            name = attr['name']
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
        
        name = handler_input.request_envelope.request.intent.slots["name"].value
        
        if name:
            speak_output = "Es ist schön dich kennenzulernen, {}. Das Spiel funktioniert folgendermaßen. Ich werde dir eine Geschichte erzählen in der Du eine entscheidende Rolle spielst. Mit deinen Entscheidungen wirst du die Geschichte leiten. Bist du bereit in das Abenteuer einzutauchen?".format(name)


            name_attributes = {
                'name': name,
            }
            attributes_manager = handler_input.attributes_manager
            attributes_manager.persistent_attributes = name_attributes
            attributes_manager.save_persistent_attributes()
        else:
            speak_output = "Es tut mir leid. Ich kenne deinen Namen nicht."

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
        speak_output = "Guten Morgen, du und dein bester Freund Erik Schneider sind Studenten an einer Hochschule. Seit Wochen arbeitet ihr fleißig an einem Gruppenprojekt, welches einen großen Teil der Endnote ausmachen wird. Ihr kommuniziert regelmäßig in der Schule... aber aus unerklärlichen Gründen ist er heute nicht aufgetaucht. Daher entscheidest du dich ihn zu kontaktieren. Willst du Erik anrufen? Erik eine Nachricht schreiben? Oder zu Erik nach Hause gehen?"
        
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

class AnrufenHandler(AbstractRequestHandler):
    """Handler for Anrufen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Anrufen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<speak> Du findest Erik in deinen Kontakten und drückst die Anruf-Taste.' + \
                        '<audio src="soundbank://soundlibrary/telephones/phone_beeps/phone_beeps_04"/>  \
                        Nach einer kurzer Pause kommt die Telefonansage. Ihr gewünschter Gesprächspartner ist zurzeit leider nicht erreichbar. Willst du etwas anderes versuchen? Du kannst zu Erik nach Hause gehen oder ihm eine Nachricht schreiben. </speak>'
        
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
        speak_output = '<speak>' + \
                        '<audio src="soundbank://soundlibrary/transportation/amzn_sfx_bicycle_bell_ring_01"/>  \
                        Während du mit deinem Fahrrad zu Erik nach Hause gefahren bist, hatte Erik einen tapferen Kampf gegen einen Grizzly Bären geliefert und verstarb. Game over.  \
                        <audio src="soundbank://soundlibrary/musical/amzn_sfx_church_bell_1x_05"/>  \
                        Willst du es erneut versuchen? Du kannst Erik anrufen oder ihm eine Nachricht schreiben. </speak>'
                        
                        
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
        speak_output = '<speak> Du schreibst eine Nachricht an Erik. Was ist los, Kumpel? Ich kann dich schon seit Stunden nicht erreichen. Schreib zurück sobald du kannst.  Das Handy vibriert, plötzlich bekommst du eine Nachricht von Erik. Während ihr miteinander schreibt, erfährst du, dass er sich irgendwo im Nirgendwo befindet und er aber froh ist mit dir zu schreiben. Du frägst ihn was das Letzte ist an was er sich erinnern kann. Erik antwortete: Ich habe im Keller...' + \
                        '<audio src="soundbank://soundlibrary/animals/amzn_sfx_bear_roar_grumble_01"/>  \
                        AAAAAA, da vorne ist ein Grizzly Bär. Was soll ich tun?! Willst du Erik schreiben, dass er wegrennen, kämpfen oder still stehen soll? </speak>'
        
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
        speak_output = '<speak> Erik läuft mitten durch den Wald. Er sieht einen Fluss.' + \
                        '<audio src="soundbank://soundlibrary/footsteps/running/running_10"/>  \
                        Beim Versuch den Fluss zu durchqueren, rutscht er auf einem glatten Stein aus. Als er sich aufrappeln will, sieht er dem Bären direkt ins Gesicht. Game Over.  \
                        <audio src="soundbank://soundlibrary/musical/amzn_sfx_church_bell_1x_05"/>  \
                        Willst du es erneut versuchen? Du kannst kämpfen oder still stehen. </speak>'
        
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
        speak_output = '<speak> Erik findet zu seiner Rechten einen großen Stein. Er nimmt den Stein, holt aus und wirft ihn mit aller Kraft auf den Bären.' + \
                        '<audio src="soundbank://soundlibrary/human/hit_punch_slap/hit_punch_slap_01"/>  \
                        Wutentbrannt läuft der Bär auf Erik zu. Was soll Erik machen? Sich totstellen oder auf den Bären springen?. </speak>'
        
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
        speak_output = '<speak> Der Bär schaut Erik an und schnüffelt ein wenig an Eriks Beinen.' + \
                        '<audio src="soundbank://soundlibrary/hospital/heartbeats_ekg/heartbeats_ekg_07"/>  \
                        Unbeeindruckt zieht der Bär an Erik vorbei und verschwindet im Gebüsch. Erik bedankt sich bei dir für den Tipp. Nun stellt sich die Frage was er machen soll. Willst du Erik schreiben, dass er ein Camp bauen soll, oder versuchen soll, aus dem Wald rauszukommen?" </speak>'
        
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
        speak_output = '<speak> Erik muss dir beichten, dass er einen schlechten Orientierungssinn hat. Er läuft über Fluss und Wälder während er mit dir schreibt. Als du ihn frägst was er eigentlich vorhin sagen wollte, erinnert er sich, dass er  im Keller eine antike Taschenuhr gefunden hat. Das nächste, woran er sich erinnert ist, dass er plötzlich im Wald war. Daraufhin rätst du ihm, die Uhr genauer anzuschauen und zu öffnen. Ein paar Minuten später ruft dich dein bester Freund an und teilt dir mit, dass er wieder zu Hause im Keller ist. Happy End' + \
                       '<audio src="soundbank://soundlibrary/gameshow/gameshow_01"/>  \
                        </speak>'
        
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
        speak_output = '<speak> Nach kurzer Zeit versammeln sich die Waldbewohner vor dem Käfig, binden Erik an einem Pfahl und bringen ihn zum Feuer.' + \
                        '<audio src="soundbank://soundlibrary/explosions/fire/fire_12"/>  \
                        Game over.  \
                        <audio src="soundbank://soundlibrary/musical/amzn_sfx_church_bell_1x_05"/>  \
                        Willst du es erneut versuchen? Du kannst noch die Ranken aufschneiden und fliehen." </speak>'

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
        speak_output = '<speak>' + \
                        '<audio src="soundbank://soundlibrary/boats_ships/sails/sails_08"/>  \
                        Erik rennt Nachschnell ins Gebüsch. einer Weile muss er dir beichten, dass er einen schlechten Orientierungssinn hat. Er läuft über Fluss und Wälder während er mit dir schreibt. Als du ihn frägst, was er eigentlich vorhin sagen wollte, erinnert er sich, dass er  im Keller eine antike Taschenuhr gefunden hat. Das nächste, woran er sich erinnert ist, dass er plötzlich im Wald war. Daraufhin rätst du ihm, die Uhr genauer anzuschauen und zu öffnen. \
                        <audio src="soundbank://soundlibrary/alarms/beeps_and_bloops/zap_03"/>  \
                        Ein paar Minuten später ruft dich dein bester Freund an und teilt dir mit, dass er wieder zu Hause im Keller ist. Happy End. \
                        <audio src="soundbank://soundlibrary/gameshow/gameshow_01"/>  \
                        </speak>'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class totstellenHandler(AbstractRequestHandler):
    """Handler for totstellen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("totstellen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<speak> Erik legt sich mit den Rücken auf den Boden und versucht sich nicht zu bewegen. Der Bär lässt sich aber nicht von Eriks Verhalten irritieren und geht in die Offensive. Als der Bär mit seiner Pfote ausholt trifft er die Taschenuhr und Erik findet sich plötzlich wieder in seinem Keller. Anscheinend war es die magische Taschenuhr die er geöffnet hatte und ihn in eine fremde Welt brachte. Erik hat sich bei dir bedankt, dass du all diese Zeit ihm beigestanden bist und er versprach nie wieder diese Uhr zu öffnen. Happy End' + \
                        '<audio src="soundbank://soundlibrary/gameshow/gameshow_01"/> \
                        </speak>'
                        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class springenHandler(AbstractRequestHandler):
    """Handler for springen Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("springen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Erik springt auf den Bären zu. Der Bär weicht zurück und und brüllt Erik an während er ihn im Kreise gehend beobachtet. Eine Flucht scheint nicht möglich zu sein. Was soll Erik machen? Sich totstellen oder die letze großoffensive starten?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class grosoffensiveHandler(AbstractRequestHandler):
    """Handler for grosoffensive Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("grosoffensive")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<speak> Erik fasst seinen ganzen Mut zusammen und rennt heroisch auf den Bären zu. Wie ein Patriot der sein Land gegen einen übermächtigen Feind dem Tode ins Auge blickend verteidigt, so muss wohl Erik sich in dem Moment gefühlt haben. Doch all seine Kraft war vergebens. Game Over.' + \
                        '<audio src="soundbank://soundlibrary/musical/amzn_sfx_church_bell_1x_05"/>  \
                        Willst du es erneut versuchen? Du kannst Erik raten sich tot zu stellen. </speak>'

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


sb = CustomSkillBuilder(persistence_adapter = dynamodb_adapter)

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
#
#other request handlers
#
sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(get_nameHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(AnrufenHandler())
sb.add_request_handler(zu_erik_nach_hause_gehenHandler())
sb.add_request_handler(SMSHandler())
sb.add_request_handler(wegrennenHandler())
sb.add_request_handler(kaempfenHandler())
sb.add_request_handler(totstellenHandler())
sb.add_request_handler(springenHandler())
sb.add_request_handler(grosoffensiveHandler())
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
