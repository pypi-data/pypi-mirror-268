import re

from bs4 import BeautifulSoup

from turandot.model import OptionalConverter, ConversionJob


class ListOfFiguresCollector(OptionalConverter):

    def check_config(self, config: dict) -> bool:
        status = bool(
            self.conversion_job.config.get_key(['opt_processors', 'list_of_figures_collector', 'enable'])
        )
        return status

    def process_step(self) -> ConversionJob:
        soup = BeautifulSoup(self.conversion_job.current_step.content, features="html5lib")
        caption_list = [i.text for i in soup.find_all("figcaption")]
        list_container = soup.new_tag("ul")
        for i in caption_list:
            item = soup.new_tag("li")
            item.string = i
            list_container.append(item)
        self.conversion_job.current_step.content = self.conversion_job.current_step.content.replace(
            self.conversion_job.config.get_key(['opt_processors', 'list_of_figures_collector', 'token']),
            list_container.prettify()
        )
        return self.conversion_job
