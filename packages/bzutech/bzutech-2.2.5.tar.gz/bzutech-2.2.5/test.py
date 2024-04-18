from bzutech import BzuTech
import asyncio

bzu = BzuTech("admin@email.com", "bzutech123")
asyncio.run(bzu.start())
print(asyncio.run(bzu.send_reading('HA-GEN-28','HA-656',25.3,'2024-04-17 10:25:02')))
