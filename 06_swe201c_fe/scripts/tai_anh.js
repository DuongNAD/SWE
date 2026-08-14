// Tải ảnh đề FE/RE/TE của forum SWE201c về máy.
//
// Chạy trong console của một tab ĐANG MỞ fuoverflow.com và ĐÃ ĐĂNG NHẬP bằng tài khoản
// có gói FUO MEMBER trở lên. Ảnh gốc nằm sau paywall: không có gói thì mọi ảnh trả 403
// ("Bạn cần nâng cấp để truy cập").
//
// Trước khi chạy:  python3 06_swe201c_fe/scripts/recv.py 8787
// Trang sẽ fetch từng ảnh (kèm cookie phiên) rồi POST base64 sang localhost:8787 để ghi
// ra 06_swe201c_fe/anh/<đề>/<số câu>.jpg. Đi đường vòng này vì cookie XenForo là HttpOnly
// (không bốc ra curl được) mà nhồi 1.094 ảnh qua kết quả tool thì vỡ context.
//
// Theo dõi tiến độ: gõ __JOB trong console.

window.__THREADS = [
 ["sp26-re","/threads/swe201c-sp26-re.6490/","RE"],
 ["sp26-fe","/threads/swe201c-sp26-fe.6390/","FE"],
 ["fa25-re","/threads/swe201c-fa25-re.5716/","RE"],
 ["fa25-fe","/threads/swe201c-fa25-fe.5657/","FE"],
 ["su25-re","/threads/swe201c-su25-re.4845/","RE"],
 ["su25-fe","/threads/swe201c-su25-fe.4739/","FE"],
 ["su2023-te2","/threads/swe201-te2-su-2023.660/","TE"],
 ["fa2024-fe","/threads/swe201c-fa-2024-fe.3132/","FE"],
 ["fa2024-re","/threads/swe201c-fa-2024-re.3172/","RE"],
 ["sp24-re","/threads/swe201c-resp24.1864/","RE"],
 ["sp24-fe","/threads/swe201c-fesp24.1822/","FE"],
 ["su2024-te2","/threads/swe201c-su-2024-te2.2603/","TE"],
 ["su2024-te1","/threads/swe201c-su-2024-te1.2555/","TE"],
 ["sp2025-re","/threads/swe201c-sp-2025-re.3804/","RE"],
 ["sp2025-fe","/threads/swe201c-sp-2025-fe.3770/","FE"],
 ["sp2023-fe","/threads/swe201c-sp-2023-fe.190/","FE"],
 ["fa2023-re","/threads/swe201-re-fa-2023.1253/","RE"],
 ["fa2022-fe","/threads/swe201c-fa-2022-fe.614/","FE"],
 ["fa2023-fe","/threads/swe201c-fe-fa-2023.1206/","FE"],
 ["su2023-fe","/threads/swe201c-fe-su-2023.617/","FE"],
 ["sp2022-fe","/threads/swe201c-sp-2022-fe.616/","FE"],
 ["su2022-fe","/threads/swe201c-su-2022-fe.615/","FE"]
];
window.__JOB = {done:0, total:0, cur:'', err:[], per:{}, running:true};

const SRV = 'http://127.0.0.1:8787/';
const b64 = b => new Promise((res, rej) => {
  const r = new FileReader();
  r.onload = () => res(r.result.split(',')[1]);
  r.onerror = rej;
  r.readAsDataURL(b);
});
const post = (de, ten, b) => fetch(SRV, {
  method: 'POST', headers: {'content-type': 'application/json'},
  body: JSON.stringify({de, ten, b64: b})
}).then(r => r.json());
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function run() {
  const J = window.__JOB;
  for (const [slug, href, loai] of window.__THREADS) {
    J.cur = slug;
    try {
      const html = await (await fetch('https://fuoverflow.com' + href, {credentials: 'include'})).text();
      const doc = new DOMParser().parseFromString(html, 'text/html');
      const posts = [...doc.querySelectorAll('article.message')];

      // Văn bản mọi bài: bài trả lời hay chứa đáp án tham khảo dạng "1a, 2b, ..."
      const txt = posts.map((p, i) => {
        const who = p.querySelector('.message-name')?.innerText.trim() || '?';
        const when = p.querySelector('time')?.getAttribute('datetime') || '';
        const body = p.querySelector('.message-body')?.innerText.replace(/\n{2,}/g, '\n').trim() || '';
        return `--- #${i + 1} ${who} ${when}\n${body}`;
      }).join('\n');
      await post('_thao_luan', slug + '.txt',
                 await b64(new Blob([`# ${slug} (${loai}) ${href}\n` + txt], {type: 'text/plain'})));

      // Chỉ lấy đính kèm của BÀI ĐẦU — đính kèm trong bài trả lời thường là ảnh khác đề.
      // Sắp theo id đính kèm tăng dần = đúng thứ tự người đăng tải lên = thứ tự câu hỏi.
      const first = posts[0] || doc;
      const seen = new Map();
      first.querySelectorAll('a[href*="/attachments/"]').forEach(a => {
        const h = a.getAttribute('href');
        const m = h.match(/\/attachments\/([^\/?]+)/); if (!m) return;
        const id = parseInt(m[1].split('.').pop(), 10); if (!id) return;
        if (!seen.has(id)) seen.set(id, {id, name: m[1], href: h});
      });
      const atts = [...seen.values()].sort((a, b) => a.id - b.id);
      J.total += atts.length; J.per[slug] = {n: atts.length, ok: 0, loai};

      let idx = 0;
      const worker = async () => {
        while (true) {
          const k = idx++; if (k >= atts.length) return;
          const a = atts[k];
          // Tên file dạng "q7-jpg.262212" thì số câu là 7; đề cũ đặt tên chung thì lấy thứ tự.
          const qm = a.name.match(/^q(\d+)-/i);
          const num = qm ? parseInt(qm[1], 10) : (k + 1);
          const ext = (a.name.match(/-(jpg|jpeg|png|webp)\./i) || [, 'jpg'])[1].toLowerCase();
          const ten = String(num).padStart(3, '0') + '.' + (ext === 'jpeg' ? 'jpg' : ext);
          for (let tri = 0; tri < 3; tri++) {
            try {
              const r = await fetch(new URL(a.href, location.origin), {credentials: 'include'});
              if (!r.ok) throw new Error('HTTP ' + r.status);   // 403 = tài khoản chưa có gói
              const blob = await r.blob();
              if (blob.size < 500) throw new Error('anh qua nho ' + blob.size);
              const res = await post(slug, ten, await b64(blob));
              if (!res.ok) throw new Error(res.loi);
              J.done++; J.per[slug].ok++;
              break;
            } catch (e) {
              if (tri === 2) { J.err.push(slug + '/' + ten + ': ' + e.message); J.done++; }
              else await sleep(700 * (tri + 1));
            }
          }
          await sleep(120);   // đừng đập server diễn đàn
        }
      };
      await Promise.all([0, 1, 2, 3].map(worker));
    } catch (e) { J.err.push(slug + ' THREAD: ' + e.message); }
  }
  J.running = false; J.cur = 'XONG';
}
run();
