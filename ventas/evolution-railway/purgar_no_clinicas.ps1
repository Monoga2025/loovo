# Purga del CRM de Railway los contactos cuyo número NO está en EVOLUTION_ALLOWED_NUMBERS (las 25 clínicas).
# Hace un respaldo en el volumen (/data/omni-antes-purga.db) antes de borrar. Ejecutar desde cualquier carpeta.
Set-Location 'C:\Users\you\Desktop\Loovo\servicios\omni-sales-crm'
$js = @'
const fs=require('fs');const {DatabaseSync}=require('node:sqlite');
fs.copyFileSync('/data/omni.db','/data/omni-antes-purga.db');
const db=new DatabaseSync('/data/omni.db');
const allowed=(process.env.EVOLUTION_ALLOWED_NUMBERS||'').split(',').map(n=>n.replace(/\D/g,'')).filter(Boolean);
if(!allowed.length){console.log('ABORT: lista vacia');process.exit(1)}
const all=db.prepare('select id,external_id from contacts').all();
const out=all.filter(c=>!allowed.includes(String(c.external_id||'').replace(/\D/g,'')));
const refs=db.prepare("select name t from sqlite_master where type='table' and sql like '%contact_id%'").all().map(r=>r.t);
for(const c of out){for(const t of refs)db.prepare('delete from '+t+' where contact_id=?').run(c.id);db.prepare('delete from contacts where id=?').run(c.id);}
console.log('antes',all.length,'purgados',out.length,'quedan',db.prepare('select count(*) n from contacts').get().n);
'@
$b64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($js))
railway ssh -s omni-crm -- node -e "eval(Buffer.from('$b64','base64').toString())"
