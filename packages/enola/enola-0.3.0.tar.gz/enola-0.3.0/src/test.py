from enola import agent
from enola.base.enola_types import ErrOrWarnKind
#from enola.base.enola_types import AgentResponseModel

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJFTk9MQV9IVUVNVUwwNC1iMTE2NjRkMWI5NmQxZGYzZjdlMzk1YWUzMzc0ZDI3MyIsImlkIjoiOWNiZTk5ZmMtZmY0Yy00MGQyLTgzYzktZDkxMmYxZThiYjM4IiwiZGlzcGxheU5hbWUiOiJ4eHgiLCJ1cmwiOiJodHRwczovL2FwaXNlbmQuZW5vbGEtYWkuY29tL2FwaSIsIm9yZ0lkIjoiRU5PTEFfSFVFTVVMMDQiLCJpYXQiOjE3MDg5NzYzMDcsImV4cCI6MTgzNTA2MDM5OSwiaXNzIjoiZW5vbGEifQ.MSuOCT0VLZTjLeL3kqiz9jl1G-coq3c3tAhbjXLft7M"
myAgent = agent.Agent(token=token, name="Ejecución Uno", isTest=True)


step1 = myAgent.new_step("step 1")

step1.add_extra_info("info1", 10)
step1.add_extra_info("info2", "valor2")

step1.add_error(id="10", message="error 1", kind=ErrOrWarnKind.INTERNAL_TOUSER)
step1.add_error(id="20", message="error 2", kind=ErrOrWarnKind.EXTERNAL)

step1.add_api_data(name="invoca algo", method="post", url="https://algo.com",  bodyToSend="bodyToSend1", headerToSend="headerToSend1", payloadReceived= "payloadReceived1", description="descripcion de la llamada")
step1.add_api_data(name="invoca 2", method="get", url="https://otrolink.com", bodyToSend="bodyToSend2", headerToSend="headerToSend2", payloadReceived= "payloadReceived2")

step1.add_file_link(name="file1", url="http://file1", sizeKb=10, type="txt")
step1.add_file_link(name="file2", url="http://file2", sizeKb=20, type="pdf")

step1.add_tag("tag1", 1)
step1.add_tag("tag2", "abc")

step1.add_warning(id="w1", message="warning1", kind=ErrOrWarnKind.EXTERNAL )
step1.add_warning(id="w2", message="warning2", kind=ErrOrWarnKind.INTERNAL_CONTROLLED )

step2 = myAgent.new_step("step 2")
step2.add_extra_info("info3", 10)
step2.add_extra_info("info4", "valor2")

step2.add_error(id="30", message="error 1", kind=ErrOrWarnKind.INTERNAL_TOUSER)
step2.add_error(id="40", message="error 2", kind=ErrOrWarnKind.EXTERNAL)

step2.add_api_data(name="invoca algo", method="post", url="https://algo.com",  bodyToSend="bodyToSend1", headerToSend="headerToSend1", payloadReceived= "payloadReceived1", description="descripcion de la llamada")
step2.add_api_data(name="invoca 2", method="get", url="https://otrolink.com", bodyToSend="bodyToSend2", headerToSend="headerToSend2", payloadReceived= "payloadReceived2")

step2.add_file_link(name="file3", url="http://file1", sizeKb=10, type="txt")
step2.add_file_link(name="file4", url="http://file2", sizeKb=20, type="pdf")

step2.add_tag("tag3", 1)
step2.add_tag("tag4", "abc")

step2.add_warning(id="w3", message="warning1", kind=ErrOrWarnKind.EXTERNAL )
step2.add_warning(id="w4", message="warning2", kind=ErrOrWarnKind.INTERNAL_CONTROLLED )

myAgent.close_step_audio(step=step1,successfull=True, audio_cost=50, audio_num=2, audio_sec=1000, audio_size=1400,step_id="123" )

myAgent.close_step_doc(step=step2,successfull=False, step_id="456", doc_char=1000, doc_cost=2000, doc_num=3000, doc_pages=4000, doc_size=5000 )
myAgent.app_id = "223",

resultado = myAgent.finish_agent(True)

print(resultado.agentDeployId)
print(resultado.enolaId)
print(resultado.enolaApiFeedback)
print(resultado.enolaUrlFeedback)
print(resultado.message)
print(resultado.successfull)
