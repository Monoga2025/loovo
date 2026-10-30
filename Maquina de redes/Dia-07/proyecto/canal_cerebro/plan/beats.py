# Beats del video A (los usan la composición y scripts/sfx.py). at(id, palabra), S(id), EN(id) en s de la línea.
B["h_con"] = at("H1", "conocimientos"); B["h_nb"] = at("H1", "NotebookLM"); B["h_bas"] = at("H2", "básicamente")
B["h_cer"] = at("H2", "cerebro"); B["h_emp"] = at("H2", "empresa")
B["cut1"] = S("C1") - 0.20                                    # invert flash 1: gancho (motion) -> pantalla
B["c1_fue"] = at("C1", "fue"); B["c1_car"] = at("C1", "carpeta"); B["c1_don"] = at("C1", "donde"); B["c1_abs"] = at("C1", "absolutamente")
B["f_in"] = S("C2a") - 0.15; B["f_age"] = at("C2a", "agente"); B["f_res"] = at("C2a", "resumen"); B["f_todo"] = at("C2a", "todo")
B["f2_in"] = S("C2b") - 0.05; B["f_md"] = at("C2b", ".md"); B["f_para"] = at("C2b", "para"); B["f_nb"] = at("C2b", "NotebookLM.")
B["u_in"] = S("C3") - 0.22; B["u_5"] = at("C3", "cinco"); B["u_y"] = at("C3", "y"); B["u_cer"] = at("C3", "cerebro.")
B["m_in"] = S("C4") - 0.18; B["m_dem"] = at("C4", "demasiada")
B["r_in"] = S("C5") - 0.06; B["r_age"] = at("C5", "agente"); B["r_rag"] = at("C5", "RAG,"); B["r_mon"] = at("C5", "montón")
B["s_in"] = S("C6") - 0.22; B["s_aca"] = at("C6", "acá")
B["l_in"] = S("C7") - 0.04; B["l_mapa"] = at("C7", "mapa"); B["l_info"] = at("C7", "infografías"); B["l_tabla"] = at("C7", "tabla")
B["q_in"] = S("C8") - 0.30; B["q_preg"] = at("C8", "preguntamos:"); B["q_t0"] = S("C9"); B["q_t1"] = EN("C9")
B["cut2"] = S("C10") - 0.20                                   # invert flash 2: pregunta (motion) -> respuesta en pantalla
B["v_in"] = S("C11") - 0.06; B["v_emp"] = at("C11", "empaquetados"); B["v_doc"] = at("C11", "documentación"); B["v_sol"] = at("C12", "soluciones"); B["v_pil"] = at("C12", "pilotos")
B["e_in"] = S("C13") - 0.22; B["e_base"] = at("C13", "base"); B["e_toda"] = at("C13", "toda"); B["e_emp"] = at("C13", "empresa.")
B["pl"] = S("PL")
