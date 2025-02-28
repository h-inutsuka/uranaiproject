from django.shortcuts import render
from django.views.generic.base import TemplateView
import random
from django.shortcuts import redirect

# モデルResultをインポート
from .models import Result

class IndexView(TemplateView):
    template_name = 'index.html'

# 大アルカナカードの説明用
class Chariot_e(TemplateView):
    template_name = 'chariot_e.html'

class Death_e(TemplateView):
    template_name = 'death_e.html'

class Devil_e(TemplateView):
    template_name = 'devil_e.html'

class Devination_e(TemplateView):
    template_name = 'devination_e.html'

class Emperor_e(TemplateView):
    template_name = 'emperor_e.html'

class Empress_e(TemplateView):
    template_name = 'empress_e.html'

class Fool_e(TemplateView):
    template_name = 'fool_e.html'

class Strength_e(TemplateView):
    template_name = 'strength_e.html'

class Fortune_e(TemplateView):
    template_name = 'fortune_e.html'

class Hermit_e(TemplateView):
    template_name = 'hermit_e.html'

class Hierophant_e(TemplateView):
    template_name = 'hierophant_e.html'

class Judgement_e(TemplateView):
    template_name = 'judgement_e.html'

class Justice_e(TemplateView):
    template_name = 'justice_e.html'

class Lover_e(TemplateView):
    template_name= 'lovers_e.html'

class Magician_e(TemplateView):
    template_name = 'magician_e.html'

class Man_e(TemplateView):
    template_name = 'man_e.html'

class Moon_e(TemplateView):
    template_name = 'moon_e.html'

class Priestess_e(TemplateView):
    template_name = 'priestess_e.html'

class Star_e(TemplateView):
    template_name = 'star_e.html'

class Sun_e(TemplateView):
    template_name = 'sun_e.html'

class Tower_e(TemplateView):
    template_name = 'tower_e.html'

class Temperance_e(TemplateView):
    template_name = 'temperance_e.html'

class World_e(TemplateView):
    template_name = 'world_e.html'


# 小アルカナ
class Wands(TemplateView):
    template_name = 'wands.html'

class Pentacles(TemplateView):
    template_name = 'pentacles.html'

class Cups(TemplateView):
    template_name = 'cups.html'

class Swords(TemplateView):
    template_name = 'swords.html'

# 大アルカナの詳細の説明
class E_one_oracle(TemplateView):
    template_name = 'E_one_oracle.html'

class E_twe_oracle(TemplateView):
    template_name = 'E_two_oracle.html'

class E_two_mind(TemplateView):
    template_name = 'E_two_mind.html'

class E_simple_cross(TemplateView):
    template_name = 'E_simple_cross.html'

class E_three_card(TemplateView):
    template_name = 'E_three_card.html'

class E_golden_trine(TemplateView):
    template_name = 'E_golden_trine.html'

class E_four_card(TemplateView):
    template_name = 'E_four_card.html'

class E_diamond_cross(TemplateView):
    template_name = 'E_diamond_cross.html'

class E_jupiter_spread(TemplateView):
    template_name = 'E_jupiter_spread.html'

class E_treasure_triangle(TemplateView):
    template_name = 'E_treasure_triangle.html'

class E_cross_spread(TemplateView):
    template_name = 'E_cross_spread.html'

class E_greek_cross(TemplateView):
    template_name = 'E_greek_cross.html'

class E_pentagram(TemplateView):
    template_name = 'E_pentagram.html'

class E_pyramid(TemplateView):
    template_name = 'E_pyramid.html'

class E_two_companies(TemplateView):
    template_name = 'E_two_companies.html'

class E_hexagram(TemplateView):
    template_name = 'E_hexagram.html'

class E_horseshoe(TemplateView):
    template_name = 'E_horseshoe.html'

class E_seven_tailings(TemplateView):
    template_name = 'E_seven_tailings.html'

class E_seven_days(TemplateView):
    template_name = 'E_seven_days.html'

class E_spiritual_spread(TemplateView):
    template_name = 'E_spiritual_spread.html'

class E_compatibility_method(TemplateView):
    template_name = 'E_compatibility_method.html'

class E_nine_card(TemplateView):
    template_name = 'E_nine_card.html'

class E_celtic_cross(TemplateView):
    template_name = 'E_celtic_cross.html'

class E_horoscope_spread(TemplateView):
    template_name = 'E_horoscope_spread.html'

# ワンオラクルのランダムURL
def random_oracle(request):
    count = Result.objects.count()  # データの総数を取得
    if count == 0:
        result = None  # データがない場合はNoneを返す
    else:
        random_index = random.randint(0, count - 1)  # 0 から (count-1) の範囲でランダムな数値を取得
        result = Result.objects.all()[random_index]  # ランダムな1件を取得
    return render(request, "one_oracle_randam.html", {"result": result})